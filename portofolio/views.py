from django.shortcuts import render


def landing_page(request):
    return render(request, "index.html")

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