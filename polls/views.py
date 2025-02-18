from django.shortcuts import render
from .models import Skill, Project, Experience, Education, Certification

def home(request):
    return render(request, 'home.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'Projects.html', {'projects': projects})

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'experience.html', {'experiences': experiences})

def education(request):
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    return render(request, 'education.html', {
        'educations': educations,
        'certifications': certifications,
    })

def contact(request):
    return render(request, 'contact.html')