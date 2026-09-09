from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Adinda Madya Aliyah",
        "npm": "2506656362",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS student at Universitas Indonesia, "
            "Passionate about business and entrepreneurship."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Adinda Madya Aliyah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)