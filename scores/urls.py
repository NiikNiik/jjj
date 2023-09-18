from django.urls import path
from . import views

urlpatterns = [
    path('connect-vibes/', views.landing_page, name='landing_page'),
]