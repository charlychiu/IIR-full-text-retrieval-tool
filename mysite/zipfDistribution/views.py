from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .file import get_file_info


def index(request):
    return render(request, 'zipfDistribution/index.html')


def load_file(request):
    get_file_name = ""
    context = ""
    if request.method == 'POST':
        get_file_name = request.POST.getlist('selected_file[]')
        context = get_file_info(get_file_name)
        # context = get_file_name

    return render(request, 'zipfDistribution/index.html', {'file_list': [get_file_name], 'context': context})
