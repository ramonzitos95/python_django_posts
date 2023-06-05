from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'text': 'Olá home',
        'title': 'Esse é a página do home'
    }

    return render(
        request,
        'home/index.html',
        context
    )