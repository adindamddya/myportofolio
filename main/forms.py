from django import forms
from django.utils.html import strip_tags
from .models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'field_of_study', 'start_year', 'end_year']

    def clean_school(self):
        school = self.cleaned_data['school']
        return strip_tags(school)
        
    def clean_degree(self):
        degree = self.cleaned_data['degree']
        return strip_tags(degree)

    def clean_field_of_study(self):
        field_of_study = self.cleaned_data.get('field_of_study', '')
        return strip_tags(field_of_study)
