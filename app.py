from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import json

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('instance.db')
    cursor = conn.cursor()
    
    # Drop existing tables to recreate with correct schema
    cursor.execute('DROP TABLE IF EXISTS recommendations')
    cursor.execute('DROP TABLE IF EXISTS survey_responses')
    cursor.execute('DROP TABLE IF EXISTS users')
    
    # Create users table
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            education_level TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create survey_responses table
    cursor.execute('''
        CREATE TABLE survey_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            favorite_subjects TEXT,
            field_preference TEXT,
            work_type TEXT,
            priority TEXT,
            learning_style TEXT,
            experience_level TEXT,
            time_commitment TEXT,
            career_timeline TEXT,
            collaboration_preference TEXT,
            work_environment TEXT,
            other_interests TEXT,
            dream_companies TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Create recommendations table
    cursor.execute('''
        CREATE TABLE recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            careers TEXT,
            skills TEXT,
            courses TEXT,
            companies TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Career recommendation logic with enhanced understanding
def get_career_recommendations(responses):
    careers = []
    skills = []
    courses = []
    companies = []
    
    subjects = responses.get('favorite_subjects', '').lower()
    field = responses.get('field_preference', '').lower()
    work_type = responses.get('work_type', '').lower()
    priority = responses.get('priority', '').lower()
    learning_style = responses.get('learning_style', '').lower()
    experience = responses.get('experience_level', '').lower()
    time_commitment = responses.get('time_commitment', '').lower()
    timeline = responses.get('career_timeline', '').lower()
    collaboration = responses.get('collaboration_preference', '').lower()
    work_env = responses.get('work_environment', '').lower()
    
    # Deep analysis based on multiple factors
    
    # Technical paths with detailed matching
    if 'technical' in field or 'both' in field:
        if 'computer' in subjects or 'math' in subjects:
            if 'beginner' in experience:
                careers.extend(['Junior Software Developer', 'Web Developer', 'IT Support Specialist'])
                skills.extend(['HTML/CSS', 'JavaScript', 'Python Basics', 'Git', 'Problem-solving'])
                courses.extend([
                    'Complete Web Development Bootcamp - Udemy',
                    'Python for Everybody - Coursera',
                    'Introduction to Programming - TechVedu',
                    'Web Development Fundamentals - Tap Academy',
                    'Coding for Beginners - BYJU\'S Future School'
                ])
                companies.extend(['Infosys', 'TCS', 'Wipro', 'Cognizant', 'Accenture'])
            elif 'intermediate' in experience or 'advanced' in experience:
                careers.extend(['Full Stack Developer', 'Software Engineer', 'DevOps Engineer', 'Cloud Engineer'])
                skills.extend(['React/Angular', 'Node.js', 'Python/Java', 'AWS/Azure', 'Docker', 'Kubernetes', 'Microservices'])
                courses.extend([
                    'Full Stack Web Development - Coursera',
                    'AWS Certified Solutions Architect - Udemy',
                    'Advanced Software Engineering - TechVedu',
                    'Cloud Computing Masterclass - Tap Academy',
                    'System Design - Coursera'
                ])
                companies.extend(['Google', 'Microsoft', 'Amazon', 'Meta', 'Apple', 'Netflix', 'Adobe'])
            
            if 'data' in work_type or 'analysis' in work_type:
                careers.extend(['Data Scientist', 'Machine Learning Engineer', 'AI Engineer', 'Data Analyst'])
                skills.extend(['Python', 'SQL', 'Machine Learning', 'TensorFlow', 'Pandas', 'NumPy', 'Statistics'])
                courses.extend([
                    'Machine Learning Specialization - Coursera',
                    'Data Science A-Z - Udemy',
                    'AI & Machine Learning - TechVedu',
                    'Python for Data Science - Tap Academy',
                    'Data Analytics Pro - BYJU\'S',
                    'Deep Learning Specialization - Coursera'
                ])
                companies.extend(['Google AI', 'DeepMind', 'OpenAI', 'Nvidia', 'Tesla', 'IBM Watson'])
        
        if 'engineering' in subjects or 'physics' in subjects:
            careers.extend(['Mechanical Engineer', 'Electrical Engineer', 'Robotics Engineer', 'Embedded Systems Engineer'])
            skills.extend(['CAD (AutoCAD/SolidWorks)', 'MATLAB', 'Circuit Design', 'Arduino/Raspberry Pi', 'C/C++'])
            courses.extend([
                'Mechanical Engineering Fundamentals - Coursera',
                'Electrical Engineering - Udemy',
                'Robotics Specialization - Coursera',
                'Embedded Systems - TechVedu',
                'Engineering Mathematics - BYJU\'S'
            ])
            companies.extend(['Tesla', 'SpaceX', 'Boeing', 'Lockheed Martin', 'General Electric', 'Siemens'])
    
    # Creative paths with depth
    if 'creative' in field or 'both' in field:
        if 'art' in subjects or 'design' in subjects:
            careers.extend(['UI/UX Designer', 'Product Designer', 'Graphic Designer', 'Motion Graphics Designer'])
            skills.extend(['Figma', 'Adobe XD', 'Photoshop', 'Illustrator', 'User Research', 'Prototyping', 'Design Thinking'])
            courses.extend([
                'UI/UX Design Specialization - Coursera',
                'Complete Graphic Design Masterclass - Udemy',
                'Product Design - TechVedu',
                'UX/UI Design Bootcamp - Tap Academy',
                'Design Thinking - Coursera',
                'Motion Graphics Pro - Udemy'
            ])
            companies.extend(['Apple', 'Google Design', 'Airbnb', 'Uber', 'Spotify', 'Adobe', 'Figma'])
        
        if 'literature' in subjects or 'writing' in subjects:
            careers.extend(['Content Writer', 'Technical Writer', 'Copywriter', 'Digital Marketing Specialist', 'SEO Specialist'])
            skills.extend(['Content Writing', 'SEO', 'Google Analytics', 'Social Media Marketing', 'Email Marketing', 'Copywriting'])
            courses.extend([
                'Content Marketing - Coursera',
                'SEO Training Masterclass - Udemy',
                'Digital Marketing Specialization - Coursera',
                'Content Writing Pro - TechVedu',
                'Copywriting Secrets - Udemy',
                'Social Media Marketing - Tap Academy'
            ])
            companies.extend(['HubSpot', 'Mailchimp', 'Salesforce', 'LinkedIn', 'Buffer', 'Hootsuite'])
    
    # Business and management
    if 'business' in subjects or 'economics' in subjects:
        if 'people' in work_type or 'team' in collaboration:
            careers.extend(['Product Manager', 'Project Manager', 'Business Analyst', 'Management Consultant'])
            skills.extend(['Product Management', 'Agile/Scrum', 'Data Analysis', 'Strategic Thinking', 'Stakeholder Management'])
            courses.extend([
                'Product Management - Coursera',
                'PMP Certification Training - Udemy',
                'Business Analysis - TechVedu',
                'Agile Project Management - Coursera',
                'Strategic Management - BYJU\'S'
            ])
            companies.extend(['McKinsey', 'BCG', 'Bain', 'Deloitte', 'PwC', 'EY', 'KPMG'])
        
        if 'high salary' in priority or 'salary' in priority:
            careers.extend(['Financial Analyst', 'Investment Banker', 'Management Consultant', 'Data Scientist'])
            skills.extend(['Financial Modeling', 'Excel', 'Python', 'SQL', 'Business Intelligence', 'PowerBI'])
            courses.extend([
                'Financial Markets - Coursera',
                'Financial Modeling & Valuation - Udemy',
                'Investment Banking - Coursera',
                'Business Intelligence - TechVedu',
                'Excel for Finance - Udemy'
            ])
            companies.extend(['Goldman Sachs', 'Morgan Stanley', 'JP Morgan', 'Citigroup', 'BlackRock'])
    
    # Cybersecurity path
    if 'computer' in subjects and ('problem' in work_type or 'security' in responses.get('other_interests', '').lower()):
        careers.extend(['Cybersecurity Analyst', 'Ethical Hacker', 'Security Engineer', 'Penetration Tester'])
        skills.extend(['Network Security', 'Ethical Hacking', 'Linux', 'Python', 'Cryptography', 'Cloud Security'])
        courses.extend([
            'Cybersecurity Specialization - Coursera',
            'Ethical Hacking - Udemy',
            'CompTIA Security+ - Udemy',
            'Cybersecurity Bootcamp - TechVedu',
            'Network Security - Tap Academy'
        ])
        companies.extend(['Palo Alto Networks', 'CrowdStrike', 'Cisco', 'Fortinet', 'Check Point'])
    
    # Mobile development
    if 'computer' in subjects and ('mobile' in work_env or 'app' in responses.get('other_interests', '').lower()):
        careers.extend(['Mobile App Developer', 'iOS Developer', 'Android Developer', 'React Native Developer'])
        skills.extend(['Swift', 'Kotlin', 'React Native', 'Flutter', 'Mobile UI/UX', 'Firebase'])
        courses.extend([
            'iOS Development - Udemy',
            'Android Development - Coursera',
            'Flutter & Dart - Udemy',
            'Mobile App Development - TechVedu',
            'React Native - Tap Academy'
        ])
        companies.extend(['Apple', 'Google', 'Uber', 'Airbnb', 'Instagram', 'WhatsApp'])
    
    # Social sciences and non-profit
    if 'social' in subjects or 'non-profit' in work_env:
        careers.extend(['HR Specialist', 'Social Worker', 'NGO Manager', 'Corporate Trainer', 'Career Counselor'])
        skills.extend(['Communication', 'Empathy', 'Training & Development', 'Conflict Resolution', 'Psychology'])
        courses.extend([
            'Human Resources Management - Coursera',
            'Psychology of Leadership - Udemy',
            'Training & Development - TechVedu',
            'Organizational Behavior - Coursera'
        ])
        companies.extend(['United Nations', 'WHO', 'Red Cross', 'Teach For India', 'Goonj'])
    
    # Startup and freelance
    if 'startup' in work_env or 'freelance' in work_env:
        careers.extend(['Freelance Developer', 'Startup Founder', 'Growth Hacker', 'Digital Nomad'])
        skills.extend(['Entrepreneurship', 'Digital Marketing', 'Full Stack Development', 'Sales', 'Networking'])
        courses.extend([
            'Startup School - Y Combinator',
            'Entrepreneurship - Coursera',
            'Growth Hacking - Udemy',
            'Freelancing Masterclass - Udemy',
            'Building Startups - TechVedu'
        ])
        companies.extend(['Y Combinator Startups', 'Techstars', 'Upwork', 'Fiverr', 'Toptal'])
    
    # Beginner-friendly recommendations
    if 'beginner' in experience:
        courses.extend([
            'Computer Science Basics - Coursera',
            'Programming for Everyone - BYJU\'S Future School',
            'Career Starter Kit - TechVedu',
            'Foundation Course - Tap Academy'
        ])
    
    # Time-based recommendations
    if '30+' in time_commitment or 'within 6' in timeline:
        courses.extend([
            'Intensive Coding Bootcamp - TechVedu',
            'Fast-Track Program - Tap Academy',
            'Crash Course Bundle - Udemy'
        ])
    
    # Remote work specific
    if 'remote' in work_env:
        careers.extend(['Remote Software Engineer', 'Digital Marketing Manager', 'Content Creator', 'Online Tutor'])
        skills.extend(['Remote Collaboration', 'Time Management', 'Async Communication', 'Self-motivation'])
    
    # Remove duplicates and limit results
    careers = list(dict.fromkeys(careers))[:8]
    skills = list(dict.fromkeys(skills))[:12]
    courses = list(dict.fromkeys(courses))[:10]
    companies = list(dict.fromkeys(companies))[:10]
    
    # Default recommendations if no matches
    if not careers:
        careers = ['Software Developer', 'Business Analyst', 'Digital Marketing Specialist', 'Product Manager']
        skills = ['Communication', 'Problem-solving', 'Adaptability', 'Critical Thinking', 'Time Management']
        courses = [
            'Career Fundamentals - Coursera',
            'Professional Skills - Udemy',
            'Industry Ready Program - TechVedu',
            'Career Launchpad - Tap Academy',
            'Skill Development - BYJU\'S'
        ]
        companies = ['Infosys', 'TCS', 'Wipro', 'Cognizant', 'Accenture', 'HCL', 'Tech Mahindra']
    
    return {
        'careers': careers,
        'skills': skills,
        'courses': courses,
        'companies': companies
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/api/submit-survey', methods=['POST'])
def submit_survey():
    try:
        data = request.json
        print("Received data:", data)  # Debug logging
        
        # Store user information
        conn = sqlite3.connect('instance.db')
        cursor = conn.cursor()
        
        # Insert user data
        cursor.execute('''
            INSERT INTO users (name, email, age, education_level)
            VALUES (?, ?, ?, ?)
        ''', (
            data.get('name'),
            data.get('email'),
            data.get('age'),
            data.get('education_level')
        ))
        
        user_id = cursor.lastrowid
        
        # Insert survey responses
        cursor.execute('''
            INSERT INTO survey_responses (user_id, favorite_subjects, field_preference, work_type, priority, 
                learning_style, experience_level, time_commitment, career_timeline, collaboration_preference, 
                work_environment, other_interests, dream_companies)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            data.get('favorite_subject s', ''),
            data.get('field_preference', ''),
            data.get('work_type', ''),
            data.get('priority', ''),
            data.get('learning_style', ''),
            data.get('experience_level', ''),
            data.get('time_commitment', ''),
            data.get('career_timeline', ''),
            data.get('collaboration_preference', ''),
            data.get('work_environment', ''),
            data.get('other_interests', ''),
            data.get('dream_companies', '')
        ))
        
        # Get recommendations
        recommendations = get_career_recommendations(data)
        
        # Store recommendations
        cursor.execute('''
            INSERT INTO recommendations (user_id, careers, skills, courses, companies)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            user_id,
            json.dumps(recommendations['careers']),
            json.dumps(recommendations['skills']),
            json.dumps(recommendations['courses']),
            json.dumps(recommendations['companies'])
        ))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'recommendations': recommendations
        })
    
    except Exception as e:
        print("Error occurred:", str(e))  # Debug logging
        import traceback
        traceback.print_exc()  # Print full error traceback
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
