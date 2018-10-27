from .models import *


def generated_raw_reverted_index(content_collection):
    for content in content_collection:
        sentence = " ".join((content.title, content.abstract))
        word_collection = str.split(sentence)
        for word in word_collection:
            if RawIndex.objects.filter(word=word).count() == 0:
                rawIndex = RawIndex.objects.create(word=word)
                rawIndex.contents.add(content)
                # print('TDIDF: Add new word into raw index')
            else:
                rawIndex = RawIndex.objects.get(word=word)
                rawIndex.contents.add(content)
                # print('TDIDF: Append new raw index to word')


def generated_porter_reverted_index(content_collection):
    for content in content_collection:
        sentence = " ".join((content.title, content.abstract))
        word_collection = str.split(sentence)
        for word in word_collection:
            if PorterIndex.objects.filter(word=word).count() == 0:
                porterIndex = PorterIndex.objects.create(word=word)
                porterIndex.contents.add(content)
                # print('TDIDF: Add new word into porter index')
            else:
                porterIndex = PorterIndex.objects.get(word=word)
                porterIndex.contents.add(content)
                # print('TDIDF: Append new porter index to word')
    pass
