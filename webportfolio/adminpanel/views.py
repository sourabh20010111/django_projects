from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from portfolio.models import About, ContactMessage, Profile, Project, Resume

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')




@login_required(login_url='login')
def manage_projects(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        project_id = request.POST.get('project_id')

        if action == 'add':
            title = request.POST.get('title')
            description = request.POST.get('description')
            github_link = request.POST.get('github_link')
            if title and description:
                Project.objects.create(title=title, description=description, github_link=github_link)

        elif action == 'edit' and project_id:
            project = get_object_or_404(Project, pk=project_id)
            project.title = request.POST.get('title')
            project.description = request.POST.get('description')
            project.github_link = request.POST.get('github_link')
            project.save()

        elif action == 'delete' and project_id:
            project = get_object_or_404(Project, pk=project_id)
            project.delete()

        return redirect('manage-projects')

    # GET request
    projects = Project.objects.all()
    return render(request, 'dashboard/manage-projects.html', {'projects': projects})


@login_required(login_url='login')
def manage_resume(request):
    resume = Resume.objects.first()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'delete' and resume:
            resume.delete()
            messages.success(request, "Resume deleted successfully!")
            return redirect('manage-resume')

        # Upload new resume
        if 'resume_file' in request.FILES:
            file = request.FILES['resume_file']
            if resume:
                resume.file.delete()  # delete old file
                resume.file = file
                resume.save()
                messages.success(request, "Resume updated successfully!")
            else:
                Resume.objects.create(file=file)
                messages.success(request, "Resume uploaded successfully!")
            return redirect('manage-resume')

    return render(request, 'dashboard/manage-resume.html', {'resume': resume})



@login_required(login_url='login')
def manage_about(request):
    about = About.objects.first()
    
    if request.method == 'POST':
        description = request.POST.get('about_text')
        skills = request.POST.get('skills')
        photo = request.FILES.get('about_photo')

        if about:
            about.description = description
            about.skills = skills
            if photo:
                about.photo = photo
            about.save()
        else:
            About.objects.create(description=description, skills=skills, photo=photo)

        return redirect('manage-about')
    return render(request, 'dashboard/manage-about.html', {'about': about})




@login_required(login_url='login')
def manage_profile(request):
    profile = Profile.objects.first()  # Assume only one profile exists

    if request.method == "POST":
        photo = request.FILES.get('profile_photo')
        if profile:
            profile.photo = photo
            profile.save()
        else:
            Profile.objects.create(photo=photo)
        messages.success(request, "Profile photo updated successfully!")
        return redirect('manage-profile')

    return render(request, 'dashboard/manage-profile.html', {
        'profile_photo': profile.photo if profile else None
    })




@login_required(login_url='login')
def manage_contact(request):
    contacts = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'dashboard/manage-contact.html',{'contacts': contacts})

@login_required(login_url='login')
def delete_contact(request, contact_id):
    if request.method == "POST":
        contact = get_object_or_404(ContactMessage, id=contact_id)
        contact.delete()
    return redirect('manage-contact')



def login_auth(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")  # adminpanel ka dashboard URL name
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "dashboard/login.html")


@login_required(login_url='login')
def logout_auth(request):
    logout(request)
    return redirect('login')


