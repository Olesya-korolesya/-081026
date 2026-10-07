#Задача1

from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.response import TemplateResponse

# def index(request):
#
#     return HttpResponse('Index')
#
# def about(request):
#
#     return HttpResponse('About')
#
# def contact(request):
#
#     return HttpResponseRedirect('/about/')
#
# def details(request):
#
#     return HttpResponsePermanentRedirect('/')

# #Задача2
#
# def support(request):
#
#     return HttpResponseRedirect(reverse('contact'))

# #Задача3
#
# def index(request):
#
#     return render(request, 'index.html')

#Задача4

def index(request):

    return TemplateResponse(request, 'index.html')

#Задача5

def profile(request):

    context = {
        'name': 'Дмитрий',
        'age': 39,
        'phone': '+79123456789',
        'email': 'dmitry@email.com'
    }

    return render(request, 'profile.html', context)