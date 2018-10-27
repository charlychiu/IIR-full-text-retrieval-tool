from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .file import read_file_in_upload_folder, file_set_generate_md5_checksum, get_documents_from_file_set
from .models import *
from .PorterStemmer import convert_sentence_through_porter
from .queries import *


def index(request):
    file_list = read_file_in_upload_folder()
    return render(request, 'zipfDistribution/index.html', {'file_list': file_list})


def load_file(request):
    raw_collection = list()
    porter_collection = list()
    if request.method == 'POST':
        get_file_name_set = request.POST.getlist('selected_file[]')
        checksum = file_set_generate_md5_checksum(get_file_name_set)
        file_set = Document.objects.filter(checksum=checksum)
        # If exist loading from database, else creating new record
        if file_set.count() > 0:
            document = file_set.get()
            raw_collection = get_content_is_raw_by_document(document)
            porter_collection = get_content_not_raw_by_document(document)
        else:
            content_collection = get_documents_from_file_set(get_file_name_set)
            document = Document.objects.create(checksum=checksum)
            for content in content_collection:
                if content[0] is None or content[1] is None:
                    continue
                if content[0].strip() == '' or content[1].strip() == '':
                    continue
                Content.objects.create(document_id=document, title=content[0], abstract=content[1],
                                       is_raw=True)

                Content.objects.create(document_id=document,
                                       title=convert_sentence_through_porter(content[0]),
                                       abstract=convert_sentence_through_porter(content[1]),
                                       is_raw=False)

            print('finish: saved to DB')
            raw_collection = get_content_is_raw_by_document(document)
            porter_collection = get_content_not_raw_by_document(document)

    return render(request, 'zipfDistribution/index.html',
                  {'raw_collection': raw_collection, 'porter_collection': porter_collection})


def create_index(request):

    pass