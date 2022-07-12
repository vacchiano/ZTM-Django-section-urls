from django.urls import path

from .views import index, greeting

urlpatterns = [
    path('', index, name='home'),
    path('hello/<str:name>/', greeting, name='greeting'),
]
