from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .file import get_porter_result, read_file_in_upload_folder


def index(request):
    file_list = read_file_in_upload_folder()
    return render(request, 'zipfDistribution/index.html', {'file_list': file_list})


def load_file(request):
    get_file_name = ""
    context = ""
    if request.method == 'POST':
        get_file_name = request.POST.getlist('selected_file[]')
        context = get_porter_result(get_file_name)
        # context = get_file_name

    return render(request, 'zipfDistribution/index.html', {'file_list': [get_file_name], 'context': context})
