# from django.urls import path
# from myapp import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('details/', views.details, name='details'),
# ]

from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
]