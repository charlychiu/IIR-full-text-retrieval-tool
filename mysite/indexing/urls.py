from django.urls import path

from . import views

app_name = 'searchEngine'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload'),
    path('load', views.load_file, name='load'),
    path('clean_pkl_cache', views.clean_pkl_cache, name='clean_pkl_cache'),
    path('clean_upload_cache', views.clean_upload_cache, name='clean_upload_cache'),
    path('search/<str:pkl_id>', views.search_keyword, name='search_keyword'),

]