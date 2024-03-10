from django.shortcuts import render


# Create your views here.
pupils = [
    {'id': 1, 'name': 'Javohir', 'last_name': 'Otaboyev',
     'm1_1': 3, 'm1_2': 5, 'm1_3': 2, 'm2_1': 5, 'm2_2': 10, 'm2_3': 5, 'm3_1': 5, 'm3_2': 5, 'all': 40},

    {'id': 2, 'name': "Firdavs", 'last_name': "Jo'rayev",
     'm1_1': 2, 'm1_2': 5, 'm1_3': 2, 'm2_1': 5, 'm2_2': 10, 'm2_3': 5, 'm3_1': 3, 'm3_2': 3, 'all': 35},

    {'id': 3, 'name': 'Samariddin', 'last_name': 'Baxtiyorov',
     'm1_1': 2, 'm1_2': 5, 'm1_3': 2, 'm2_1': 3, 'm2_2': 10, 'm2_3': 1, 'm3_1': 5, 'm3_2': 3, 'all': 31},

    {'id': 4, 'name': 'Sunnatullo', 'last_name': 'Sharipov',
     'm1_1': 3, 'm1_2': 5, 'm1_3': 2, 'm2_1': 5, 'm2_2': 10, 'm2_3': 5, 'm3_1': 5, 'm3_2': 5, 'all': 40},

    {'id': 5, 'name': 'Zafarbek', 'last_name': 'Olimov',
     'm1_1': 3, 'm1_2': 5, 'm1_3': 2, 'm2_1': 5, 'm2_2': 10, 'm2_3': 4, 'm3_1': 5, 'm3_2': 5, 'all': 39},

    {'id': 6, 'name': 'Ozodbek', 'last_name': 'Ahrorov',
     'm1_1': 2, 'm1_2': 5, 'm1_3': 1, 'm2_1': 4, 'm2_2': 10, 'm2_3': 5, 'm3_1': 5, 'm3_2': 5, 'all': 37},
]


def pupils_show(request):
    global pupils
    return render(request, 'home_pupils.html', {'pupils': pupils})


def pupil_show(request, id):
    global pupils
    print([pupils[id-1]])
    return render(request, 'pupil.html', {'pupils': [pupils[id - 1]]})
