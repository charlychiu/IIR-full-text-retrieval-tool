from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .forms import UploadFileForm
from .file import save_file_from_post, read_file_in_upload_folder, get_file_info, clean_tmp_pkl, clean_upload_file, \
    search_from_tmp_pkl


def upload_file(request):
    context = ""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_file_from_post(request.FILES['file_input'])

    return HttpResponseRedirect(reverse('searchEngine:index'))


def load_file(request):
    get_file_name = ""
    context = ""
    if request.method == 'POST':
        get_file_name = request.POST.getlist('selected_file[]')
        context = get_file_info(get_file_name)
        # context = get_file_name

    return render(request, 'searchEngine/index.html', {'file_list': [get_file_name], 'context': context})


def clean_pkl_cache(request):
    clean_tmp_pkl()
    return HttpResponseRedirect(reverse('searchEngine:index'))


def clean_upload_cache(request):
    clean_upload_file()
    return HttpResponseRedirect(reverse('searchEngine:index'))


def search_keyword(request, pkl_id):
    keyword = request.POST['search_keyword']
    result_list = search_from_tmp_pkl(pkl_id, str.strip(keyword).lower())
    return render(request, 'searchEngine/result.html',
                  {'result_list': result_list, 'context': '', 'keyword': str.strip(keyword)})


def index(request):
    file_list = read_file_in_upload_folder()
    context = ''
    return render(request, 'searchEngine/index.html', {'file_list': file_list, 'context': context})
