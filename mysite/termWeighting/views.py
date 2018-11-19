from django.shortcuts import render

from .file import *
from .tfidf import *


# Create your views here.
def index(request):
    file_list = read_file_in_upload_folder()
    context = ''
    return render(request, 'termWeighting/index.html', {'file_list': file_list, 'context': context})


def load_file(request):
    get_file_name = ""
    context = ""
    if request.method == 'POST':
        get_file_name = request.POST.getlist('selected_file[]')
        context = get_file_info(get_file_name)
        pkl_id = context[-2]
        input_data = combine_title_and_abstract(context[0])
        context = tfidf_with_norm(input_data)
        # print(context[1])  # each index present each doc and its tfidf
        return render(request, 'termWeighting/index.html',
                      {'file_list': [get_file_name], 'context': context, 'pkl_id': pkl_id})


def preview_document(request, pkl_id, doc_index):
    result_doc = retrieval_from_tmp_pkl(pkl_id, doc_index)
    return render(request, 'termWeighting/result.html', {'result_doc': result_doc})
