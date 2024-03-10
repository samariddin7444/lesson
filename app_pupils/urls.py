from django.urls import path

from .views import pupils_show, pupil_show


urlpatterns = [
    path('', pupils_show, name='pupils'),
    path('<int:id>/', pupil_show, name='pupil')
]