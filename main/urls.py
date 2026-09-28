from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_education,
    create_education,
    edit_education,
    delete_education,
    get_education_json,
    register_user,
    login_user,
    logout_user,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<int:education_id>/edit/", edit_education, name="edit_education"),
    path("education/<int:education_id>/delete/", delete_education, name="delete_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]