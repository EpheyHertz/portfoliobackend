from rest_framework import generics,status
from .models import Project, Skill, Education, Experience, Certification, Contact, Testimonial
from .serializers import ProjectSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, CertificationSerializer, ContactSerializer, TestimonialSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import logging
import tempfile 
import os
from pathlib import Path
import b2sdk.v2 as b2
from django.conf import settings

logger = logging.getLogger(__name__)
# Project Views
class WelcomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to Ephey Portfolio APIs"})
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        # Ensure that only an image is uploaded
        if 'image' in self.request.FILES:
            image_file = self.request.FILES['image']

            if not image_file.content_type.startswith('image/'):
                raise ValidationError("Only image files are allowed.")

            # Upload the image to Backblaze
            try:
                # Authorize and initialize B2 API
                application_key_id = settings.AWS_ACCESS_KEY_ID
                application_key = settings.AWS_SECRET_ACCESS_KEY

                info = b2.InMemoryAccountInfo()
                b2_api = b2.B2Api(info)
                b2_api.authorize_account("production", application_key_id, application_key)

                # Get the Backblaze bucket
                bucket = b2_api.get_bucket_by_name(settings.AWS_STORAGE_BUCKET_NAME)

                # Save the uploaded image to a temporary location
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(image_file.read())  # Write image data to temp file
                    temp_file.flush()

                # Upload the file to Backblaze
                uploaded_file = bucket.upload_local_file(
                        local_file=temp_file.name,
                        file_name=f'images/{image_file.name}'
                 )

                # Delete the local temporary file after upload
                image_url = b2_api.get_download_url_for_fileid(uploaded_file.id_)
                # Get the public URL for the uploaded image
                # image_url = f'{settings.AWS_S3_ENDPOINT_URL}/file/{settings.AWS_STORAGE_BUCKET_NAME}/images/{image_file.name}'
                
                # Save the project with the image URL in the database
                serializer.save(image_url=image_url)

            except Exception as e:
                logger.error(f"Error uploading file to Backblaze: {e}")
                raise ValidationError(f"Error uploading file: {e}")
        else:
            raise ValidationError("No image file found.")


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        project = self.get_object()
        
        # If a new image is uploaded, check its type
        if 'image' in self.request.data:
            image_file = self.request.data['image']
            if not image_file.content_type.startswith('image/'):
                raise ValidationError("Only image files are allowed.")
            
            # If the project has an existing image, delete it before saving the new one
            if project.image:
                project.image.delete()  # This removes the old image from Backblaze
        
            # Create a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in image_file.chunks():
                    temp_file.write(chunk)
                temp_file_path = temp_file.name
            
            # Upload the new image to Backblaze
            application_key_id = settings.AWS_ACCESS_KEY_ID
            application_key = settings.AWS_SECRET_ACCESS_KEY
            info = b2.InMemoryAccountInfo()
            b2_api = b2.B2Api(info)
            b2_api.authorize_account("production", application_key_id, application_key)

            bucket = b2_api.get_bucket_by_name(settings.AWS_STORAGE_BUCKET_NAME)
            uploaded_file = bucket.upload_local_file(local_file=temp_file_path, file_name=image_file.name)

            # Store the URL in the project instance
            project.image_url = b2_api.get_download_url_for_fileid(uploaded_file.id_)

            # Optionally, remove the temporary file after uploading
            os.remove(temp_file_path)

        # Save the updated project with the new image URL
        serializer.save()
    def perform_destroy(self, instance):
        # Delete the image from Backblaze before deleting the project
        if instance.image:
            instance.image.delete()  # This will remove the image from Backblaze
        
        # Now delete the project
        instance.delete()

# Skill Views
class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'id'


# Education Views
class EducationListCreateView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    lookup_field = 'id'


# Experience Views
class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    lookup_field = 'id'


# Certification Views
class CertificationListCreateView(generics.ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class CertificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    lookup_field = 'id'


# Contact Views
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'


# Testimonial Views

class TestimonialListCreateView(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def perform_create(self, serializer):
        # Ensure that only an image is uploaded
        if 'photo' in self.request.FILES:
            photo_file = self.request.FILES['photo']

            if not photo_file.content_type.startswith('image/'):
                raise ValidationError("Only image files are allowed.")

            # Upload the image to Backblaze
            try:
                # Authorize and initialize B2 API
                application_key_id = settings.AWS_ACCESS_KEY_ID
                application_key = settings.AWS_SECRET_ACCESS_KEY

                info = b2.InMemoryAccountInfo()
                b2_api = b2.B2Api(info)
                b2_api.authorize_account("production", application_key_id, application_key)

                # Get the Backblaze bucket
                bucket = b2_api.get_bucket_by_name(settings.AWS_STORAGE_BUCKET_NAME)

                # Save the uploaded image to a temporary location
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(photo_file.read())  # Write image data to temp file
                    temp_file.flush()

                # Upload the file to Backblaze
                uploaded_file = bucket.upload_local_file(
                        local_file=temp_file.name,
                        file_name=f'photos/{photo_file.name}'
                 )

                # Delete the local temporary file after upload
                photo_url = b2_api.get_download_url_for_fileid(uploaded_file.id_)
                # Get the public URL for the uploaded image
                # image_url = f'{settings.AWS_S3_ENDPOINT_URL}/file/{settings.AWS_STORAGE_BUCKET_NAME}/images/{image_file.name}'
                
                # Save the project with the image URL in the database
                serializer.save(photo_url=photo_url)

            except Exception as e:
                logger.error(f"Error uploading file to Backblaze: {e}")
                raise ValidationError(f"Error uploading file: {e}")
        else:
            raise ValidationError("No image file found.")

class TestimonialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    lookup_field = 'id'
    def perform_update(self, serializer):
        testimonial = self.get_object()
        
        # If a new image is uploaded, check its type
        if 'photo' in self.request.data:
            photo_file = self.request.data['photo']
            if not photo_file.content_type.startswith('image/'):
                raise ValidationError("Only image files are allowed.")
            
            # If the project has an existing image, delete it before saving the new one
            if testimonial.photo:
                testimonial.photo.delete()  # This removes the old image from Backblaze
        
            # Create a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in photo_file.chunks():
                    temp_file.write(chunk)
                temp_file_path = temp_file.name
            
            # Upload the new image to Backblaze
            application_key_id = settings.AWS_ACCESS_KEY_ID
            application_key = settings.AWS_SECRET_ACCESS_KEY
            info = b2.InMemoryAccountInfo()
            b2_api = b2.B2Api(info)
            b2_api.authorize_account("production", application_key_id, application_key)

            bucket = b2_api.get_bucket_by_name(settings.AWS_STORAGE_BUCKET_NAME)
            uploaded_file = bucket.upload_local_file(local_file=temp_file_path, file_name=photo_file.name)

            # Store the URL in the project instance
            testimonial.photo_url = b2_api.get_download_url_for_fileid(uploaded_file.id_)

            # Optionally, remove the temporary file after uploading
            os.remove(temp_file_path)

        # Save the updated project with the new image URL
        serializer.save()
    def perform_destroy(self, instance):
        # Delete the image from Backblaze before deleting the project
        if instance.photo:
            instance.photo.delete()  # This will remove the image from Backblaze
        
        # Now delete the project
        instance.delete()

