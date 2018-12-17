from django.urls import path

from . import views

app_name = 'indexing'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('load', views.load_file, name='load'),
    path('BSBI', views.bsbi, name='bsbi'),
    path('spimi', views.spimi, name='spimi'),
    path('search_keyword', views.search_keyword, name='search_keyword')
]