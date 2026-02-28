from django.urls import path
from .views import home
from . import views   # ✅ THIS LINE WAS MISSING

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

urlpatterns = [
    path('', home, name='home'),
]