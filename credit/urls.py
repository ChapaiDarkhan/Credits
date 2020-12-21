from django.urls import path
from . import views

urlpatterns = [
    path('', views.create),
    path('create', views.create, name='create'),
]
