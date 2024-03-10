from django.urls import path

from .views import themes_show


urlpatterns = [
    path('', themes_show, name='themes'),
]