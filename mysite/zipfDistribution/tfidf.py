from .models import *


def generated_raw_index(content_collection):
    for content in content_collection:
        sentence = " ".join((content.title, content.abstract))
        word_collection = str.split(sentence)
        for word in word_collection:
            rawIndex = RawIndex.objects.create(word=word)
            rawIndex.contents.add(content)
            print('TDIDF: Add new word into raw index')
    pass


def generated_porter_index(content_collection):
    pass
