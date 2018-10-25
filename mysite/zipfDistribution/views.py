from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .file import read_file_in_upload_folder, file_set_generate_md5_checksum, get_documents_from_file_set
from .models import Document, Content
from .PorterStemmer import convert_sentence_through_porter


def index(request):
    file_list = read_file_in_upload_folder()
    return render(request, 'zipfDistribution/index.html', {'file_list': file_list})


def load_file(request):
    if request.method == 'POST':
        get_file_name_set = request.POST.getlist('selected_file[]')
        checksum = file_set_generate_md5_checksum(get_file_name_set)
        file_set = Document.objects.filter(checksum=checksum)
        # If exist loading from database, else creating new record
        if file_set.count() > 0:
            load_result = file_set.get().contents.all()
        else:
            content_collection = get_documents_from_file_set(get_file_name_set)
            document = Document.objects.create(checksum=checksum)
            document.save()
            for content in content_collection:
                if content[0] is None or content[1] is None:
                    continue
                if content[0].strip() == '' or content[1].strip() == '':
                    continue
                saved_content = Content.objects.create(document_id=document, title=content[0], abstract=content[1],
                                                       is_raw=True)
                saved_content.save()
                saved_content1 = Content.objects.create(document_id=document,
                                                        title=convert_sentence_through_porter(content[0]),
                                                        abstract=convert_sentence_through_porter(content[1]),
                                                        is_raw=False)
                saved_content1.save()
            print('finish: saved to DB')
            load_result = document.contents.all()

    return render(request, 'zipfDistribution/index.html', {'document_list': load_result})
