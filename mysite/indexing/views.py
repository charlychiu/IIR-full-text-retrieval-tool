from django.shortcuts import render
from .file import *
from .models import *
import re
import math
import time


# Create your views here.

def index(request):
    file_list = read_file_in_upload_folder()
    context = ''
    return render(request, 'indexing/index.html', {'file_list': file_list, 'context': context})


def search_keyword(request):
    keyword = request.POST['search_keyword']
    inverse_index = SPIMI.objects.filter(word=keyword)[:1].get().documents
    # print(inverse_index.replace("{", " ").replace("}", " ").replace(",", ""))
    inverse_index = inverse_index.replace("{", " ").replace("}", " ").replace(",", "").strip().split(' ')
    # print(inverse_index)
    doc_list = list()
    for idx in inverse_index:
        doc = Document.objects.get(pk=idx)
        count_str = doc.title + ' ' + doc.abstract
        doc_list.append([idx, count_str.count(keyword)+count_str.count(keyword.capitalize()), count_str])
    doc_list.sort(key=lambda x: x[1], reverse=True)
    print(doc_list[:5])
    return render(request, 'indexing/index.html', {'context': doc_list[:5]})



def load_file(request):
    if request.method == 'POST':
        get_file_name = request.POST.getlist('selected_file[]')
        context = get_file_info(get_file_name)

        # Save to DB
        # for doc in context[0]:
        #     if doc[0] is None or doc[1] is None:
        #         continue
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


# def bsbi_word2hash(document_list):
#     word_hash_table_mapping = dict()
#     for doc in document_list:
#         word_set = doc[1].split()
#         for word in word_set:
#             word_hash_table_mapping[hash(word)] = word
#
#     for k, v in word_hash_table_mapping.items():
#         # temp_dict[k] = sorted(v)
#         bsbi_map = BSBI_Map(hash=k, word=v)
#         bsbi_map.save()
#         print('save to db')

def spimi_processing(document_list):
    word_inverse_index = dict()
    for doc in document_list:
        word_set = doc[1].split()
        for word in word_set:
            set_pool = word_inverse_index.get(word, set())
            set_pool.add(doc[0])
            word_inverse_index[word] = set_pool

    for k, v in word_inverse_index.items():
        # temp_dict[k] = sorted(v)
        spimi_model = SPIMI(word=k, documents=str(v))
        spimi_model.save()

        # word_inverse_index[word] = doc[0]
        # spimi_model = SPIMI(word=word, documents=doc[0])
        # spimi_model.save()


def bsbi_word2hash_indexing(document_list):
    word_hash_table_mapping = dict()
    for doc in document_list:
        word_set = doc[1].split()
        for word in word_set:
            word_hash_table_mapping[hash(word)] = word
            bsbi_model = BSBI(word=hash(word), documents=doc[0])
            bsbi_model.save()

    # Do merge
    bsbi_merge()

    for k, v in word_hash_table_mapping.items():
        bsbi_map = BSBI_Map(hash=k, word=v)
        bsbi_map.save()
        print('save to db')
    # print(word_hash_table_mapping)
    return word_hash_table_mapping


def bsbi_merge():
    bsbi_raw = BSBI.objects.all()
    temp_dict = dict()
    for record in bsbi_raw:
        set_pool = temp_dict.get(record.word, set())
        set_pool.add(record.documents)
        temp_dict[record.word] = set_pool
    for k, v in temp_dict.items():
        # temp_dict[k] = sorted(v)
        bsbi = BSBI_Merge(word=k, documents=str(sorted(v)))
        bsbi.save()
        # print('save to db')
    # print(temp_dict)


def bsbi(request):
    # bsbi_merge()
    start = time.time()
    document_set = get_doc_list()
    # bsbi_word2hash_indexing(document_set)  # 1929.9404311180115
    # spimi_processing(document_set)  # 80.82763957977295
    end = time.time()
    print(end - start)
    # bsbi_word2hash(document_set)
    # chunk_doc_set = chunks(document_set, 2)

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
