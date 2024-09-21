from django.urls import path
from django.conf import settings

from .views import (
    ProjectListCreateView, ProjectDetailView,
    SkillListCreateView, SkillDetailView,
    EducationListCreateView, EducationDetailView,
    ExperienceListCreateView, ExperienceDetailView,
    CertificationListCreateView, CertificationDetailView,
    ContactListCreateView, ContactDetailView,
    TestimonialListCreateView, TestimonialDetailView,WelcomeView
)

urlpatterns = [
    # Project URLs
    path('',WelcomeView.as_view(), name='welcome'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<uuid:id>/', ProjectDetailView.as_view(), name='project-detail'),

    # Skill URLs
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<uuid:id>/', SkillDetailView.as_view(), name='skill-detail'),

    # Education URLs
    path('education/', EducationListCreateView.as_view(), name='education-list-create'),
    path('education/<uuid:id>/', EducationDetailView.as_view(), name='education-detail'),

    # Experience URLs
    path('experience/', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('experience/<uuid:id>/', ExperienceDetailView.as_view(), name='experience-detail'),

    # Certification URLs
    path('certifications/', CertificationListCreateView.as_view(), name='certification-list-create'),
    path('certifications/<uuid:id>/', CertificationDetailView.as_view(), name='certification-detail'),

    # Contact URLs
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<uuid:id>/', ContactDetailView.as_view(), name='contact-detail'),

    # Testimonial URLs
    path('testimonials/', TestimonialListCreateView.as_view(), name='testimonial-list-create'),
    path('testimonials/<uuid:id>/', TestimonialDetailView.as_view(), name='testimonial-detail'),
]
