from django.forms import ModelForm, TextInput, NumberInput

from main.models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school",
            "degree",
            "field_of_study",
            "start_year",
            "end_year",
        ]

        labels = {
            "school": "School",
            "degree": "Degree",
            "field_of_study": "Field of Study",
            "start_year": "Start Year",
            "end_year": "End Year",
        }

        widgets = {
            "school": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "Bachelor's Degree",
                }
            ),
            "field_of_study": TextInput(
                attrs={
                    "placeholder": "Information System",
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2025",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2029",
                }
            ),
        }