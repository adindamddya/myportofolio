from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import EducationForm
from main.models import Education, Experience


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


def show_education(request):
    response = get_education_json(request)
    education_data = list(
        serializers.deserialize("json", response.content)
    )
    education_list = [item.object for item in education_data]

    context = {
        "name": "Adinda Madya Aliyah",
        "education_list": education_list,
    }
    return render(request, "education.html", context)


def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Adinda Madya Aliyah",
        "form": form,
    }
    return render(request, "education_form.html", context)


def edit_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Adinda Madya Aliyah",
        "form": form,
        "education": education,
        "is_edit": True,
    }
    return render(request, "education_form.html", context)


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")

    return redirect("main:show_education")


def get_education_json(request):
    education = Education.objects.all()
    education_json = serializers.serialize("json", education)
    return HttpResponse(
        education_json,
        content_type="application/json",
    )