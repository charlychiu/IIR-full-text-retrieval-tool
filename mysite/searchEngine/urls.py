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
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]