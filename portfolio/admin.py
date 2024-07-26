from django.contrib import admin
from .models import Project, Skill, ContactMessage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'timestamp')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'timestamp')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
