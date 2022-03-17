
from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('eduform/', AddEdu.as_view(), name='add-edu'),
    path('proform/', AddPro.as_view(),name='add-pro'),
    path('skillform/', AddSkill.as_view(), name='add-skill'),
    path('pdf/<pk>/', pdf_view),
    path('eduform/detail/<int:pk>', DetailedEdu.as_view(),name="detailed-edu"),
    path('projectform/detail/<int:pk>', DetailedPro.as_view(),name="detailed-project"),
    path('skillform/detail/<int:pk>', DetailedSkill.as_view(),name="detailed-skill"),
    path('eduform/detail/<int:pk>/update', UpdateEdu.as_view(),name="update-edu"),
    path('eduform/detail/<int:pk>/delete', DeleteEdu.as_view(),name="delete-edu"),
    path('proform/detail/<int:pk>/update', UpdatePro.as_view(),name="update-pro"),
    path('proform/detail/<int:pk>/delete', DeletePro.as_view(),name="delete-pro"),
    path('skillform/detail/<int:pk>/update', UpdateSkill.as_view(),name="update-skill"),
    path('skillform/detail/<int:pk>/delete', DeleteSkill.as_view(),name="delete-skill"),

]