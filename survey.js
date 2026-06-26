let currentStep = 1;
const totalSteps = 12;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    showStep(currentStep);
    updateProgress();
});

// Show specific step
function showStep(step) {
    const steps = document.querySelectorAll('.form-step');
    steps.forEach((s, index) => {
        if (index + 1 === step) {
            s.classList.add('active');
            setTimeout(() => s.classList.add('visible'), 50);
        } else {
            s.classList.remove('active', 'visible');
        }
    });
    
    // Update buttons
    document.getElementById('prevBtn').style.display = step === 1 ? 'none' : 'inline-block';
    document.getElementById('nextBtn').style.display = step === totalSteps ? 'none' : 'inline-block';
    document.getElementById('submitBtn').style.display = step === totalSteps ? 'inline-block' : 'none';
    
    // Update step indicator
    document.getElementById('currentStep').textContent = step;
    document.getElementById('totalSteps').textContent = totalSteps;
    
    updateProgress();
}

// Change step
function changeStep(direction) {
    const currentStepElement = document.querySelector(`.form-step[data-step="${currentStep}"]`);
    
    // Validate current step before proceeding
    if (direction === 1 && !validateStep(currentStep)) {
        return;
    }
    
    currentStep += direction;
    
    if (currentStep < 1) {
        currentStep = 1;
    }
    if (currentStep > totalSteps) {
        currentStep = totalSteps;
    }
    
    showStep(currentStep);
}

// Validate step
function validateStep(step) {
    const stepElement = document.querySelector(`.form-step[data-step="${step}"]`);
    
    if (step === 1) {
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const age = document.getElementById('age').value;
        const education = document.getElementById('education_level').value;
        
        if (!name || !email || !age || !education) {
            showError('Please fill in all required fields');
            return false;
        }
        
        if (!isValidEmail(email)) {
            showError('Please enter a valid email address');
            return false;
        }
        
        if (age < 15 || age > 50) {
            showError('Age must be between 15 and 50');
            return false;
        }
    }
    
    if (step === 2) {
        const checkedBoxes = stepElement.querySelectorAll('input[name="subjects"]:checked');
        if (checkedBoxes.length === 0) {
            showError('Please select at least one subject');
            return false;
        }
    }
    
    if (step === 3 || step === 4 || step === 5 || step === 6 || step === 7 || step === 8 || step === 9 || step === 10) {
        const inputs = stepElement.querySelectorAll('input[required]');
        let isValid = false;
        inputs.forEach(input => {
            if (input.checked) isValid = true;
        });
        if (!isValid) {
            showError('Please select an option');
            return false;
        }
    }
    
    if (step === 11) {
        const checkedBoxes = stepElement.querySelectorAll('input[name="work_environment"]:checked');
        if (checkedBoxes.length === 0) {
            showError('Please select at least one work environment');
            return false;
        }
    }
    
    return true;
}

// Email validation
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Show error message
function showError(message) {
    // Remove existing error if any
    const existingError = document.querySelector('.error-message');
    if (existingError) {
        existingError.remove();
    }
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
    
    const stepContent = document.querySelector('.form-step.active .step-content');
    stepContent.insertBefore(errorDiv, stepContent.firstChild);
    
    setTimeout(() => {
        errorDiv.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        errorDiv.classList.remove('show');
        setTimeout(() => errorDiv.remove(), 300);
    }, 4000);
}

// Update progress bar
function updateProgress() {
    const progress = (currentStep / totalSteps) * 100;
    document.getElementById('progressFill').style.width = progress + '%';
}

// Form submission
document.getElementById('surveyForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    if (!validateStep(currentStep)) {
        return;
    }
    
    // Collect form data
    const formData = {
        name: document.getElementById('name').value.trim(),
        email: document.getElementById('email').value.trim(),
        age: parseInt(document.getElementById('age').value),
        education_level: document.getElementById('education_level').value,
        favorite_subjects: Array.from(document.querySelectorAll('input[name="subjects"]:checked'))
            .map(cb => cb.value).join(', '),
        field_preference: document.querySelector('input[name="field_preference"]:checked').value,
        work_type: document.querySelector('input[name="work_type"]:checked').value,
        priority: document.querySelector('input[name="priority"]:checked').value,
        learning_style: document.querySelector('input[name="learning_style"]:checked').value,
        experience_level: document.querySelector('input[name="experience_level"]:checked').value,
        time_commitment: document.querySelector('input[name="time_commitment"]:checked').value,
        career_timeline: document.querySelector('input[name="career_timeline"]:checked').value,
        collaboration_preference: document.querySelector('input[name="collaboration_preference"]:checked').value,
        work_environment: Array.from(document.querySelectorAll('input[name="work_environment"]:checked'))
            .map(cb => cb.value).join(', '),
        other_interests: document.getElementById('other_interests').value.trim(),
        dream_companies: document.getElementById('dream_companies').value.trim()
    };
    
    // Show loading overlay
    document.getElementById('loadingOverlay').style.display = 'flex';
    
    try {
        const response = await fetch('/api/submit-survey', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Store recommendations in sessionStorage
            sessionStorage.setItem('careerRecommendations', JSON.stringify(result.recommendations));
            
            // Redirect to results page
            setTimeout(() => {
                window.location.href = '/results';
            }, 1500);
        } else {
            document.getElementById('loadingOverlay').style.display = 'none';
            showError('An error occurred. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('loadingOverlay').style.display = 'none';
        showError('Network error. Please check your connection and try again.');
    }
});

// Add click animation to cards
document.querySelectorAll('.checkbox-card, .radio-card').forEach(card => {
    card.addEventListener('click', function() {
        this.classList.add('clicked');
        setTimeout(() => this.classList.remove('clicked'), 300);
    });
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' && currentStep < totalSteps) {
        changeStep(1);
    } else if (e.key === 'ArrowLeft' && currentStep > 1) {
        changeStep(-1);
    }
});
