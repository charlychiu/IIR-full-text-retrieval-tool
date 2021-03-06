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
        context_sublinear = tfidf_with_sublinear(input_data)
        context_without_norm = tfidf_without_norm(input_data)
        # print(input_data)
        sentence_set_processed = cut_document_set_to_sentence(input_data)
        # print(sentence_set_processed)
        context_sentence = tfidf_with_norm(sentence_set_processed)

        search_result_collection = list()
        if request.POST['search_keyword'] is not None and request.POST['search_keyword'] != '':
            search_result_collection = keyword_search_for_tfidf_ranking(input_data, request.POST['search_keyword'])
            # print(search_result_collection)
            search_result_collection.sort(key=lambda x: x[1], reverse=True)
            print(search_result_collection)

        # print(context[1])  # each index present each doc and its tfidf
        return render(request, 'termWeighting/index.html',
                      {'file_list': [get_file_name], 'context': context, 'pkl_id': pkl_id,
                       'context_sublinear': context_sublinear,
                       'context_without_norm': context_without_norm,
                       'context_sentence': context_sentence, 'search_result_collection': search_result_collection})


def preview_document(request, pkl_id, doc_index):
    result_doc = retrieval_from_tmp_pkl(pkl_id, doc_index)
    return render(request, 'termWeighting/result.html', {'result_doc': result_doc})


def preview_document_correct_index(request, pkl_id, doc_index):
    result_doc = retrieval_from_tmp_pkl(pkl_id, int(doc_index) + 1)
    return render(request, 'termWeighting/result.html', {'result_doc': result_doc})
