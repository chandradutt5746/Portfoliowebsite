from rest_framework import serializers
from .models import Project, Skill, ContactMessage


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Project
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
