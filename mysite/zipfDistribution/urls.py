from django.urls import path

from . import views

app_name = 'zipfDistribution'
urlpatterns = [
    path('', views.index, name='index'),
    path('load', views.load_file, name='load'),
    path('chart', views.zipf_chart, name='chart'),
    path('search', views.search_by_keyword, name='search'),
    path('result/<word>/<search_type>', views.result_of_search, name='result'),

]