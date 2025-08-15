from django.contrib import admin

# Register your models here.
# portfolio/admin.py
from .models import ContactMessage,About, Project,Profile, Resume

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "updated_at")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('photo', 'updated_at')

admin.site.register(Profile, ProfileAdmin)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')