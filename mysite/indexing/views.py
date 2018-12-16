from django.shortcuts import render
from .file import *
from .models import *
import re
import math


# Create your views here.

def index(request):
    file_list = read_file_in_upload_folder()
    context = ''
    return render(request, 'indexing/index.html', {'file_list': file_list, 'context': context})


def load_file(request):
    if request.method == 'POST':
        get_file_name = request.POST.getlist('selected_file[]')
        context = get_file_info(get_file_name)

        # Save to DB
        # for doc in context[0]:
        #     doc_model = Document(title=doc[0], abstract=doc[1])
        #     doc_model.save()
        print(len(context[0][1]))
        print(context[0][1])
        return render(request, 'indexing/index.html', {'file_list': '', 'context': context})
    pass


def get_doc_list():
    document = Document.objects.all()
    full_document_list = list()
    for doc in document:
        full_context = doc.title + doc.abstract
        full_context = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*():;><]+", " ", full_context)
        full_document_list.append([doc.id, full_context])
    return full_document_list


def chunks(arr, m):
    n = int(math.ceil(len(arr) / float(m)))
    return [arr[i:i + n] for i in range(0, len(arr), n)]


def bsbi_word2hash_indexing(document_list):
    word_hash_table_mapping = dict()
    for doc in document_list:
        word_set = doc[1].split()
        for word in word_set:
            word_hash_table_mapping[hash(word)] = word
            bsbi_model = BSBI(word=hash(word), documents=doc[0])
            bsbi_model.save()
    # print(word_hash_table_mapping)
    return word_hash_table_mapping


def bsbi(request):
    document_set = get_doc_list()
    chunk_doc_set = chunks(document_set, 2)
    # a = bsbi_word2hash_indexing(chunk_doc_set[1])
    # print(a)
    # print(len(part1_doc_set))
    # print(len(part1_doc_set[0]))
    # print(len(part1_doc_set[1]))
    # part2_doc_set = document_set[len(document_set) // 2 + 1:len(document_set) // 2]
    # print(document_set)
    pass


def spimi(request):
    pass
