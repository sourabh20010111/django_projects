# portfolio/views.py
from django.shortcuts import render, redirect
from .models import ContactMessage,About, Project,Profile, Resume

def home(request):
    # Success message (contact form)
    success_message = ""
    if request.GET.get('success') == '1':
        success_message = "Your message has been sent successfully!"

    projects = Project.objects.all()  # Fetch projects

    profile = Profile.objects.first()

    resume = Resume.objects.last()

    # About data
    about = About.objects.first()
    skills = [s.strip() for s in about.skills.split(',')] if about and about.skills else []

    context = {
        'success_message': success_message,
        'about': about,
        'skills': skills,
        'projects': projects,
        'profile': profile,
        'resume': resume,
    }

    return render(request, 'portfolio/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            # Redirect to home with success flag and anchor
            return redirect('/?success=1#contact')

    # If accessed directly
    return redirect('/#contact')