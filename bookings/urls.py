from django.urls import path
from .views import book_service

urlpatterns = [
    path('book/<int:id>/', book_service, name='book'),
]