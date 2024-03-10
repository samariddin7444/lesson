from django.urls import path, re_path
from .views import week_days_all, week_days, error404


urlpatterns = [
    path('<str:domen>/', week_days, name='week_days'),
    path('', week_days_all, name='week_days_all'),
    re_path('^', error404, name='error404')
]