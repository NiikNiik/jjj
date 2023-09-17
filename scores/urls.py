from django.urls import path
from . import views

urlpatterns = [
    path('vibes/', views.landing_page, name='landing_page'),
]