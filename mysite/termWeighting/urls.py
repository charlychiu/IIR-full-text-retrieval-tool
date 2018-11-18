from django.urls import path

from . import views

app_name = 'termWeighting'
urlpatterns = [
    path('', views.index, name='index'),
    path('load', views.load_file, name='load'),
]