from django.contrib import admin
from .models import Project, Skill, Education, Experience, Certification, Contact, Testimonial

# Custom admin for Project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

# Custom admin for Skill model
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    search_fields = ('name',)

# Custom admin for Education model
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year')
    search_fields = ('institution', 'degree')

# Custom admin for Experience model
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date')
    search_fields = ('position', 'company')

# Custom admin for Certification model
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authority', 'issue_date')
    search_fields = ('title', 'authority')

# Custom admin for Contact model
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'linkedin', 'github', 'twitter')
    search_fields = ('email', 'linkedin', 'github')

# Custom admin for Testimonial model (optional)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'company')
    search_fields = ('name', 'role', 'company')

# Register all models with custom admin configurations
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
