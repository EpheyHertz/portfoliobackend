import uuid
from django.db import models

# Project model
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for primary key
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.JSONField(default=list, blank=True, null=True)  # Make sure default is a valid list
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # To store project screenshots
    link = models.URLField(blank=True, null=True)  # Link to the project (GitHub or live demo)
    demolink = models.URLField(blank=True, null=True)  # Link to the project (GitHub or live demo)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Skill model
class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for primary key
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Choose from Frontend, Backend, DevOps, etc.
    proficiency = models.IntegerField(default=0)  # Rate skill from 1-100 (e.g., 80 for proficiency)

    def __str__(self):
        return self.name

# Education model
class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for primary key
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField(null=True, blank=True)  # End year can be null if ongoing

    def __str__(self):
        return f"{self.degree} - {self.institution}"

# Experience model
class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for primary key
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Can be null for ongoing jobs

    def __str__(self):
        return f"{self.position} at {self.company}"

# Certification model
class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for primary key
    title = models.CharField(max_length=100)
    authority = models.CharField(max_length=100)  # Issuer of the certificate (e.g., Coursera, Udemy)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)  # URL to the certificate (optional)

    def __str__(self):
        return self.title

# Contact model
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for primary key
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email

# Testimonial model
class Testimonial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for primary key
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()  # The testimonial content
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"
