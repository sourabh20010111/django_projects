# portfolio/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class About(models.Model):
    photo = models.ImageField(upload_to='about/', blank=True, null=True)
    description = models.TextField()
    skills = models.TextField(blank=True, help_text="Comma-separated (e.g. Manual, Automation, Selenium)")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Section"

    def skill_list(self):
        return [s.strip() for s in (self.skills or "").split(",") if s.strip()]

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    photo = models.ImageField(upload_to='profile_photos/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Profile Photo"

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"


