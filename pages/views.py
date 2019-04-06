from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hellollo Word </h1>')
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about page',
        'my_number': 123,
        'my_list': [123, 1231, 312, 123123, 'abc']
    }
    return render(request, 'about.html', my_context)


def social_view(request, *args, **kwargs):
    return render(request, 'home.html', {})
