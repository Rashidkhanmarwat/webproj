from django.contrib import admin
from django.urls import path
from student import views
from .views import *
urlpatterns = [
    path("", home),
    path("home/", home),
    path("stdadd/",stdadd),   
    path("delete-std/<int:id>",deletestd),
    path("update-std/<int:id>",updatestd),
    path("do-update-std/",doupdatestd),

    ]

