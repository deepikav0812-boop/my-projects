# Career Path Guide AI Chatbot

A modern, AI-powered career guidance chatbot that helps students discover their perfect career path through personalized recommendations.

## Features

- 🎯 **Personalized Career Recommendations** - Based on interests, strengths, and preferences
- 🧠 **Rule-Based AI Logic** - Intelligent matching algorithm
- 📊 **SQLite Database** - Stores user data and responses
- 🎨 **Modern UI/UX** - Smooth animations and responsive design
- 📱 **Mobile Friendly** - Works on all devices
- 📈 **Skill & Course Suggestions** - Curated learning resources

## Tech Stack

### Frontend
- HTML5
- CSS3 / SCSS
- JavaScript (ES6+)
- Fetch API for backend communication

### Backend
- Python 3.8+
- Flask Framework
- SQLite Database
- Pandas for data handling

## Project Structure

```
Career_Guide/
├── app.py                  # Flask application
├── instance.db            # SQLite database (auto-created)
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   ├── style.css     # Compiled CSS
│   │   └── style.scss    # Source SCSS
│   └── js/
│       ├── main.js       # Homepage scripts
│       ├── survey.js     # Survey page scripts
│       └── results.js    # Results page scripts
└── templates/
    ├── index.html        # Homepage
    ├── survey.html       # Survey/questionnaire
    └── results.html      # Results page
```

## Installation

1. **Clone or download the project**

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   Navigate to: `http://localhost:5000`

## How It Works

### User Flow
1. **Homepage** - Learn about the importance of career guidance
2. **Survey** - Answer 6 steps of questions about interests and preferences
3. **AI Analysis** - Rule-based logic matches responses to career paths
4. **Results** - Personalized career recommendations with skills and courses
5. **Database** - All responses stored in SQLite for future reference

### Survey Questions
- Personal Information (Name, Email, Age, Education)
- Favorite Subjects
- Technical vs Creative Preference
- Type of Work
- Salary vs Work-Life Balance Priority
- Additional Interests

### Career Recommendation Logic
The app uses rule-based conditions to match:
- Subject interests → Career domains
- Field preferences → Technical/Creative paths
- Work type → Job characteristics
- Priorities → Career attributes

## Database Schema

### Tables

**users**
- id (Primary Key)
- name
- email
- age
- education_level
- timestamp

**survey_responses**
- id (Primary Key)
- user_id (Foreign Key)
- favorite_subjects
- field_preference
- work_type
- priority
- other_interests
- timestamp

**recommendations**
- id (Primary Key)
- user_id (Foreign Key)
- careers (JSON)
- skills (JSON)
- courses (JSON)
- timestamp

## Customization

### Adding New Career Paths
Edit the `get_career_recommendations()` function in `app.py`:

```python
if 'your_condition' in field:
    careers.extend(['New Career 1', 'New Career 2'])
    skills.extend(['Skill 1', 'Skill 2'])
    courses.extend(['Course Name - Platform'])
```

### Styling
Modify `static/css/style.scss` and compile to CSS, or directly edit `style.css`

### Database Location
The SQLite database (`instance.db`) is created in the project root directory.

## Features in Detail

### 🎨 Modern UI
- Gradient backgrounds
- Smooth animations
- Floating particles effect
- Interactive card selections
- Progress indicators
- Loading states

### 📊 Data Storage
- User information saved to database
- Survey responses tracked
- Recommendations logged
- Timestamp tracking

### 🚀 Performance
- Optimized JavaScript
- Lazy loading animations
- Efficient database queries
- Session storage for results

## Browser Support
- Chrome (recommended)
- Firefox
- Safari
- Edge

## Future Enhancements
- [ ] Machine Learning model integration
- [ ] User authentication
- [ ] Career path comparison
- [ ] LinkedIn integration
- [ ] Export to PDF
- [ ] Email notifications
- [ ] Admin dashboard

## License
MIT License - Feel free to use for educational purposes

## Contact
For questions or support, please reach out to your development team.

---

**Made with ❤️ for students seeking career guidance**
