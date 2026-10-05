from django.urls import path
from . import views

from main.views import (
    show_main,
    show_experience,
    show_education,
    create_education,
    edit_education,
    delete_education,
    get_education_json,
    add_education_ajax,
    delete_education_ajax,
    register_user,
    login_user,
    logout_user,
    toggle_star,
)

app_name = "main"

urlpatterns = [
    # Main
    path("", show_main, name="show_main"),

    # Experience
    path("experience/", show_experience, name="show_experience"),

    # Education
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path(
        "education/<int:id>/edit/",
        edit_education,
        name="edit_education",
    ),
    path(
        "education/<int:id>/delete/",
        delete_education,
        name="delete_education",
    ),
    path(
        "education/<int:id>/star/",
        toggle_star,
        name="toggle_star",
    ),

    # Education AJAX
    path(
        "education/json/",
        get_education_json,
        name="get_education_json",
    ),
    path(
        "education/add-ajax/",
        add_education_ajax,
        name="add_education_ajax",
    ),
    path(
        "education/delete-ajax/<int:id>/",
        delete_education_ajax,
        name="delete_education_ajax",
    ),

    # Authentication
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]