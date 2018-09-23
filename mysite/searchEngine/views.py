from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .forms import UploadFileForm
from .file import save_file_from_post
from .file import read_file_in_upload_folder


def upload_file(request):
    context = ""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_file_from_post(request.FILES['file_input'])
            # return HttpResponseRedirect('/searchEngine')
            # return HttpResponseRedirect(reverse('searchEngine:upload'))  # best way redirect

    return HttpResponseRedirect(reverse('searchEngine:index'))


def load_file(request):
    get_file_name = ""
    context = ""
    if request.method == 'POST':
        get_file_name = request.POST['selected_file']
        context = get_file_name

    return render(request, 'searchEngine/index.html', {'file_list': [get_file_name], 'context': context})


def index(request):
    file_list = read_file_in_upload_folder()
    context = ''
    return render(request, 'searchEngine/index.html', {'file_list': file_list, 'context': context})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
