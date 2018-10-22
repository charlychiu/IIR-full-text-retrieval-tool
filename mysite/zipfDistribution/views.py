from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .file import get_porter_result, read_file_in_upload_folder, file_list_with_md5
from .models import Document, Content
from .PorterStemmer import convert_sentence_through_porter


def index(request):
    file_list = read_file_in_upload_folder()
    return render(request, 'zipfDistribution/index.html', {'file_list': file_list})


def load_file(request):
    get_file_name = ""
    context = ""
    if request.method == 'POST':
        get_file_name = request.POST.getlist('selected_file[]')
        context = get_porter_result(get_file_name)
        checksum = file_list_with_md5(get_file_name)
        document = Document.objects.create(checksum=checksum)
        document.save()
        for i in context:
            if i[0] is None or i[1] is None:
                continue
            if i[0].strip() == '' or i[1].strip() == '':
                continue
            content = Content.objects.create(document_id=document, title=convert_sentence_through_porter(i[0]), abstract=convert_sentence_through_porter(i[1]))
            # print(convert_sentence_through_porter(i[0]))
            content.save()
        print('finish')
        # context = get_file_name

    return render(request, 'zipfDistribution/index.html')
