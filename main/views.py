from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST # <--- INI YANG BARU DITAMBAHKAN
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User

from main.forms import EducationForm
from main.models import Education, Experience
import datetime

def show_main(request):
    last_login = request.COOKIES.get(
        "last_login",
        "Belum ada sesi login / Cookie tidak ditemukan"
    )

    context = {
        "name": "Adinda Madya Aliyah",
        "npm": "2506656362",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS student at Universitas Indonesia, "
            "Passionate about business and entrepreneurship."
        ),
        "last_login": last_login,
    }

    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name  ": "Adinda Madya Aliyah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_education(request):
    # Halaman ini sekarang hanya merender kerangka HTML kosong (skeleton)
    return render(request, 'education.html')

def get_education_json(request):
    query = request.GET.get('search', '')
    
    if query:
        educations = Education.objects.filter(school__icontains=query) 
    else:
        educations = Education.objects.all()

    data = []
    for edu in educations:
        is_starred = request.user in edu.starred_by.all() if request.user.is_authenticated else False
        
        data.append({
            'id': edu.id,
            'school': edu.school, 
            'degree': edu.degree,
            'stars_count': edu.starred_by.count(),
            'is_starred': is_starred,
        })
    return JsonResponse(data, safe=False)

def add_education_ajax(request):
    if request.method == 'POST':
        if not request.user.is_superuser: 
            return JsonResponse({'status': 'error', 'message': 'Kamu tidak memiliki izin untuk menambah data.'}, status=403)

        form = EducationForm(request.POST)
        if form.is_valid():
            edu = form.save()
            return JsonResponse({'status': 'success', 'message': 'Data pendidikan berhasil ditambahkan!'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'message': form.errors}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Metode HTTP tidak diizinkan.'}, status=400)

@require_POST
def delete_education_ajax(request, id):
    if not request.user.is_superuser:
        return JsonResponse({'status': 'error', 'message': 'Akses ditolak.'}, status=403)
        
    try:
        edu = get_object_or_404(Education, pk=id)
        edu.delete()
        return JsonResponse({'status': 'success', 'message': 'Data berhasil dihapus.'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


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
    school_query = request.GET.get("school", "").strip()

    education = Education.objects.prefetch_related("starred_by").all()

    if school_query:
        education = education.filter(school__icontains=school_query)

    data = []

    for item in education:
        starred_users = item.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        starred_by_names = ", ".join(
            [user.username for user in starred_users]
        )

        data.append({
            "pk": str(item.id),
            "fields": {
                "school": item.school,
                "degree": item.degree,
                "field_of_study": item.field_of_study,
                "start_year": item.start_year,
                "end_year": item.end_year,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            },
        })

    return JsonResponse(data, safe=False)

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat!")
            return redirect("main:login")

    context = {
        "name": "Adinda Madya Aliyah",
        "form": form,
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())

        response = redirect("main:show_main")
        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        return response

    context = {
        "name": "Adinda Madya Aliyah",
        "form": form,
    }

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)

    response = redirect("main:show_main")
    response.delete_cookie("last_login")

    return response

@login_required(login_url="/login/")
def toggle_star(request, education_id):
    if request.method != "POST":
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)

    if education.starred_by.filter(pk=request.user.pk).exists():
        education.starred_by.remove(request.user)
    else:
        education.starred_by.add(request.user)

    return redirect("main:show_education")