import os

from django.shortcuts import render


# Create your views here.
def themes_show(request):
    with open(f'{os.getcwd()}/app_themes/fayls_txt/themes', 'r') as f:
        themes_list = []
        for theme in f:
            theme = theme.replace('\n', '')
            if len(theme) > 0:
                themes_list.append(theme)
    return render(request, 'themes.html', context={'themes_list': themes_list})
