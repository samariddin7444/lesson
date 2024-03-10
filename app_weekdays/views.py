from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

weekdays = [
    {'uz': 'Dushanba', 'ru': 'понедельник', 'en': 'Sunday'},
    {'uz': 'Seshanba', 'ru': 'вторник', 'en': 'Monday'},
    {'uz': 'Chorshanba', 'ru': 'Среда', 'en': 'Tuesday'},
    {'uz': 'Payshanba', 'ru': 'Четверг', 'en': 'Wednesday'},
    {'uz': 'Juma', 'ru': 'Пятница', 'en': 'Thursday'},
    {'uz': 'Shanba', 'ru': 'Суббота', 'en': 'Friday'},
    {'uz': 'Yakshanba', 'ru': 'Воскресенье', 'en': 'Saturday'},
]


def week_days_all(request):
    global weekdays
    return render(request, 'all_week_days.html', context={'weekdays': weekdays})


def week_days(request, domen):
    if domen in ['uz', 'ru', 'en']:
        if domen == 'uz':
            language = 'UZBEKISTAN'
        if domen == 'ru':
            language = 'RUSSIAN'
        if domen == 'en':
            language = 'ENGLISH'
        global weekdays
        return render(request, 'week_days.html',
                      context={'weekdays': weekdays, 'domen': domen, 'language': language})

    return HttpResponse('404 Not Found', status=404)


def error404(request):
    return HttpResponse('404 Not Found', status=404)