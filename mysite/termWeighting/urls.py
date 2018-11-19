from django.urls import path

from . import views

app_name = 'termWeighting'
urlpatterns = [
    path('', views.index, name='index'),
    path('load', views.load_file, name='load'),
    path('preview/<str:pkl_id>/<str:doc_index>', views.preview_document, name='preview_document'),
    path('previewIndex/<str:pkl_id>/<str:doc_index>', views.preview_document_correct_index, name='preview_document_index'),
]