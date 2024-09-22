from rest_framework import serializers
from django.conf import settings
from .models import Project,Skill,Education,Experience,Certification,Contact,Testimonial

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(required=False)  # Allow image uploads

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technologies', 'image', 'image_url', 'link', 'demolink', 'created_at']
        read_only_fields = ['created_at']

    def get_image(self, obj):
        # Ensure that the image URL is correctly formatted without localhost or other unwanted URLs
        if obj.image:
            image_url = obj.image.url  # Get the image URL from the model

            # Exclude localhost and specific backend URLs
            if "127.0.0.1" in image_url or "localhost" in image_url or "epheyhertzportfoliobackend.onrender.com" in image_url:
                # Replace these with the correct Backblaze URL
                image_url = image_url.replace("http://127.0.0.1:8000/", "")
                image_url = image_url.replace("https://epheyhertzportfoliobackend.onrender.com/", "")

            return image_url  # Return the correctly formatted Backblaze URL
        return None



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
    id = serializers.UUIDField(read_only=True)
    photo = serializers.ImageField(required=False)  # Allow photo uploads

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'title', 'company', 'text', 'photo', 'photo_url']
        read_only_fields = ['id', 'photo_url']

    def get_photo_url(self, obj):
        # Ensure that the photo URL is correctly formatted
        return obj.photo.url if obj.photo else None