from .models import RawIndexTwitter, PorterIndexTwitter, RawIndex, PorterIndex
import nltk
import operator


def generated_raw_index_frequency(content_collection):
    for content in content_collection:
        sentence = " ".join((content.title, content.abstract))
        word_collection = str.split(sentence)
        for word in word_collection:
            rawIndex = RawIndex.objects.get(word=word)
            rawIndex.frequency += 1
            rawIndex.save()


def generated_porter_index_frequency(content_collection):
    for content in content_collection:
        sentence = " ".join((content.title, content.abstract))
        word_collection = str.split(sentence)
        for word in word_collection:
            porterIndex = PorterIndex.objects.get(word=word)
            porterIndex.frequency += 1
            porterIndex.save()


def generated_raw_reverted_index(content_collection):
    for content in content_collection:
        sentence = " ".join((content.title, content.abstract))
        word_collection = str.split(sentence)
        for word in word_collection:
            if RawIndexTwitter.objects.filter(word=word).count() == 0:
                rawIndexTwitter = RawIndexTwitter.objects.create(word=word)
                rawIndexTwitter.contents.add(content)
                # print('TDIDF: Add new word into raw index')
            else:
                rawIndexTwitter = RawIndexTwitter.objects.get(word=word)
                rawIndexTwitter.contents.add(content)
                # print('TDIDF: Append new raw index to word')


def generated_porter_reverted_index(content_collection):
    for content in content_collection:
        sentence = " ".join((content.title, content.abstract))
        word_collection = str.split(sentence)
        for word in word_collection:
            if PorterIndexTwitter.objects.filter(word=word).count() == 0:
                porterIndexTwitter = PorterIndexTwitter.objects.create(word=word)
                porterIndexTwitter.contents.add(content)
                # print('TDIDF: Add new word into porter index')
            else:
                porterIndexTwitter = PorterIndexTwitter.objects.get(word=word)
                porterIndexTwitter.contents.add(content)
                # print('TDIDF: Append new porter index to word')


def get_edit_distance(keyword, model):
    words = model.objects.values_list('word', flat=True)
    result = {}
    for word in words:
        ed = nltk.edit_distance(keyword, word)
        result[word] = ed
    result = sorted(result.items(), key=operator.itemgetter(1))
    if result[0] == 0:
        return result[0]
    else:
        return result[:5]
