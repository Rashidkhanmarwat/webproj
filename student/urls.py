from django.contrib import admin
from django.urls import path
from student import views
from .views import *
urlpatterns = [
    # path("", views.student, name = 'home'),
    # path("student", views.student, name = 'student'),
    path("", home),
    path("home/", home),
    path("stdadd/",stdadd), ]

