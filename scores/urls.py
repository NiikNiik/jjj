from django.urls import path
from . import views

urlpatterns = [
    path('discover-vibes/', views.landing_page, name='landing_page'),
]