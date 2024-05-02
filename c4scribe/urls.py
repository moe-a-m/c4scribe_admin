from django.urls import path
from c4scribe import views

urlpatterns = [
    path('', views.generate_text, name='generate_text'),
]