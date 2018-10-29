from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .file import read_file_in_upload_folder, file_set_generate_md5_checksum, get_documents_from_file_set
from .models import *
from .PorterStemmer import convert_sentence_through_porter
from .queries import *
from .tfidf import *
from django.db.models import Count
from django.http import JsonResponse
import operator
import nltk


def index(request):
    file_list = read_file_in_upload_folder()
    return render(request, 'zipfDistribution/index.html', {'file_list': file_list})


def load_file(request):
    raw_collection = list()
    porter_collection = list()
    if request.method == 'POST':
        get_file_name_set = request.POST.getlist('selected_file[]')
        checksum = file_set_generate_md5_checksum(get_file_name_set)
        file_set = Document.objects.filter(checksum=checksum)
        # If exist loading from database, else creating new record
        if file_set.count() > 0:
            document = file_set.get()
            raw_collection = get_content_is_raw_by_document(document)
            porter_collection = get_content_not_raw_by_document(document)
            generated_raw_index_frequency(raw_collection)
            generated_porter_index_frequency(porter_collection)
            # generated_raw_reverted_index(raw_collection)
            # generated_porter_reverted_index(porter_collection)
            # pass
        else:
            content_collection = get_documents_from_file_set(get_file_name_set)
            document = Document.objects.create(checksum=checksum)
            for content in content_collection:
                # if content[0] is None or content[1] is None:
                #     continue
                # if content[0].strip() == '' or content[1].strip() == '':
                #     continue
                Content.objects.create(document_id=document, title='', abstract=content[0].translate(
                    {ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}),
                                       is_raw=True)

                Content.objects.create(document_id=document,
                                       title='',
                                       abstract=convert_sentence_through_porter(content[0].translate(
                                           {ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})),
                                       is_raw=False)

            print('finish: saved to DB')
            raw_collection = get_content_is_raw_by_document(document)
            porter_collection = get_content_not_raw_by_document(document)
            # generated_raw_reverted_index(raw_collection)
            # generated_porter_reverted_index(porter_collection)

    return render(request, 'zipfDistribution/index.html',
                  {'raw_collection': raw_collection, 'porter_collection': porter_collection})


def zipf_chart(request):
    # discussion only appear more than 300 times
    rawIndex = RawIndex.objects.annotate(frq_count=Count('contents')).filter(frq_count__gt=300)
    result = {}
    for word in rawIndex:
        result[word.word] = word.frq_count
    result = sorted(result.items(), key=operator.itemgetter(1))
    result.reverse()

    porterIndex = PorterIndex.objects.annotate(frq_count=Count('contents')).filter(frq_count__gt=300)
    result1 = {}
    for word in porterIndex:
        result1[word.word] = word.frq_count
    result1 = sorted(result1.items(), key=operator.itemgetter(1))
    result1.reverse()

    return render(request, 'zipfDistribution/chart.html',
                  {'result': result, 'result1': result1, 'raw_count': get_objects_count(RawIndex),
                   'porter_count': get_objects_count(PorterIndex)})


def zipf_chart_twitter(request):
    rawIndex = RawIndexTwitter.objects.annotate(frq_count=Count('contents')).filter(frq_count__gt=300)
    result = {}
    for word in rawIndex:
        result[word.word] = word.frq_count
    result = sorted(result.items(), key=operator.itemgetter(1))
    result.reverse()

    porterIndex = PorterIndexTwitter.objects.annotate(frq_count=Count('contents')).filter(frq_count__gt=300)
    result1 = {}
    for word in porterIndex:
        result1[word.word] = word.frq_count
    result1 = sorted(result1.items(), key=operator.itemgetter(1))
    result1.reverse()
    return render(request, 'zipfDistribution/chart.html',
                  {'result': result, 'result1': result1, 'raw_count': get_objects_count(RawIndexTwitter),
                   'porter_count': get_objects_count(PorterIndexTwitter)})


def search_by_keyword(request):
    # two type match => using raw index or porter index
    if request.method == 'GET':
        return render(request, 'zipfDistribution/search.html')
    if request.method == 'POST':
        keyword = request.POST['search_keyword']
        raw_result = get_edit_distance(keyword, RawIndex)
        porter_result = get_edit_distance(convert_sentence_through_porter(keyword + ' '), PorterIndex)
        print(raw_result)
        print(porter_result)
        return render(request, 'zipfDistribution/search.html',
                      {'raw_result': raw_result, 'porter_result': porter_result})


def result_of_search(request, word, search_type):
    print(word, search_type)
    # Using search_type to distinguish which index table
    if search_type == '1':
        result_list = RawIndex.objects.get(word=word).contents.all()
    if search_type == '2':
        result_list = PorterIndex.objects.get(word=word).contents.all()

    print(result_list[0].abstract)

    return render(request, 'zipfDistribution/result.html',
                  {'result_list': result_list, 'result_count': result_list.count()})
