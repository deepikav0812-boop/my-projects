// Load and display results
document.addEventListener('DOMContentLoaded', () => {
    const recommendations = JSON.parse(sessionStorage.getItem('careerRecommendations'));
    
    if (!recommendations) {
        window.location.href = '/survey';
        return;
    }
    
    displayCareers(recommendations.careers);
    displaySkills(recommendations.skills);
    displayCourses(recommendations.courses);
    displayCompanies(recommendations.companies);
    
    // Animate results on load
    animateResults();
});

// Display career recommendations
function displayCareers(careers) {
    const careersList = document.getElementById('careersList');
    careersList.innerHTML = '';
    
    const icons = [
        'fa-laptop-code',
        'fa-chart-line',
        'fa-paint-brush',
        'fa-briefcase',
        'fa-rocket',
        'fa-brain',
        'fa-database',
        'fa-users'
    ];
    
    careers.forEach((career, index) => {
        const careerCard = document.createElement('div');
        careerCard.className = 'career-item';
        careerCard.style.animationDelay = `${index * 0.1}s`;
        careerCard.innerHTML = `
            <div class="career-icon">
                <i class="fas ${icons[index % icons.length]}"></i>
            </div>
            <h3>${career}</h3>
            <button class="learn-more-btn" onclick="searchCareer('${career}')">
                Learn More <i class="fas fa-external-link-alt"></i>
            </button>
        `;
        careersList.appendChild(careerCard);
    });
}

// Display skills
function displaySkills(skills) {
    const skillsList = document.getElementById('skillsList');
    skillsList.innerHTML = '';
    
    skills.forEach((skill, index) => {
        const skillBadge = document.createElement('div');
        skillBadge.className = 'skill-badge';
        skillBadge.style.animationDelay = `${index * 0.05}s`;
        skillBadge.innerHTML = `
            <i class="fas fa-check-circle"></i>
            <span>${skill}</span>
        `;
        skillsList.appendChild(skillBadge);
    });
}

// Display courses
function displayCourses(courses) {
    const coursesList = document.getElementById('coursesList');
    coursesList.innerHTML = '';
    
    const platforms = {
        'Coursera': { icon: 'fa-graduation-cap', color: '#0056D2' },
        'Udemy': { icon: 'fa-play-circle', color: '#A435F0' },
        'edX': { icon: 'fa-book', color: '#02262B' },
        'LinkedIn': { icon: 'fa-linkedin', color: '#0077B5' },
        'TechVedu': { icon: 'fa-code', color: '#FF6B6B' },
        'Tap Academy': { icon: 'fa-chalkboard-teacher', color: '#4ECDC4' },
        'BYJU': { icon: 'fa-user-graduate', color: '#9B59B6' },
        'Y Combinator': { icon: 'fa-rocket', color: '#FF6600' }
    };
    
    courses.forEach((course, index) => {
        let platform = 'Coursera';
        for (let p in platforms) {
            if (course.includes(p)) {
                platform = p;
                break;
            }
        }
        
        const courseItem = document.createElement('div');
        courseItem.className = 'course-item';
        courseItem.style.animationDelay = `${index * 0.1}s`;
        courseItem.innerHTML = `
            <div class="course-icon" style="background: ${platforms[platform].color}">
                <i class="fas ${platforms[platform].icon}"></i>
            </div>
            <div class="course-info">
                <h4>${course}</h4>
                <span class="course-platform">${platform}</span>
            </div>
            <button class="enroll-btn" onclick="searchCourse('${course.replace(/'/g, "\\'")}')">
                <i class="fas fa-external-link-alt"></i>
            </button>
        `;
        coursesList.appendChild(courseItem);
    });
}

// Display companies
function displayCompanies(companies) {
    const companiesList = document.getElementById('companiesList');
    companiesList.innerHTML = '';
    
    if (!companies || companies.length === 0) {
        companiesList.innerHTML = '<p class="no-data">Company recommendations will be personalized based on your profile.</p>';
        return;
    }
    
    companies.forEach((company, index) => {
        const companyCard = document.createElement('div');
        companyCard.className = 'company-item';
        companyCard.style.animationDelay = `${index * 0.1}s`;
        companyCard.innerHTML = `
            <div class="company-logo">
                <i class="fas fa-building"></i>
            </div>
            <h4>${company}</h4>
            <button class="company-btn" onclick="searchCompany('${company.replace(/'/g, "\\'")}')">
                View Careers <i class="fas fa-arrow-right"></i>
            </button>
        `;
        companiesList.appendChild(companyCard);
    });
}

// Search for company careers
function searchCompany(company) {
    const searchQuery = encodeURIComponent(`${company} careers jobs openings`);
    window.open(`https://www.google.com/search?q=${searchQuery}`, '_blank');
}

// Search for career information
function searchCareer(career) {
    const searchQuery = encodeURIComponent(`${career} career path salary requirements`);
    window.open(`https://www.google.com/search?q=${searchQuery}`, '_blank');
}

// Search for course
function searchCourse(course) {
    const searchQuery = encodeURIComponent(course);
    window.open(`https://www.google.com/search?q=${searchQuery}`, '_blank');
}

// Animate results
function animateResults() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    document.querySelectorAll('.result-card').forEach(card => {
        observer.observe(card);
    });
}

// Confetti animation on page load
function createConfetti() {
    const colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b'];
    const confettiCount = 50;
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 3 + 's';
        confetti.style.animationDuration = (Math.random() * 3 + 2) + 's';
        document.body.appendChild(confetti);
        
        setTimeout(() => confetti.remove(), 5000);
    }
}

// Show confetti on load
window.addEventListener('load', () => {
    createConfetti();
});
