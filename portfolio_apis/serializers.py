from rest_framework import serializers
from .models import Project,Skill,Education,Experience,Certification,Contact,Testimonial

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Explicitly specify UUID for id

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technologies', 'image', 'link','demolink', 'created_at']
        read_only_fields = ['created_at']


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Explicitly specify UUID for id

    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'proficiency']

class EducationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Explicitly specify UUID for id

    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'field_of_study', 'start_year', 'end_year']


class ExperienceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Explicitly specify UUID for id

    class Meta:
        model = Experience
        fields = ['id', 'company', 'position', 'description', 'start_date', 'end_date']


class CertificationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Explicitly specify UUID for id

    class Meta:
        model = Certification
        fields = ['id', 'title', 'authority', 'issue_date', 'expiration_date', 'link']

class ContactSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Explicitly specify UUID for id

    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone', 'linkedin', 'github', 'twitter']

class TestimonialSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Explicitly specify UUID for id

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role','company','title', 'text', 'photo']