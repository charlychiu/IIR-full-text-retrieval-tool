from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras import backend
import pandas as pd
import numpy as np


# all type context input like: [['article', 'abstract']]


def count_string_of_character(context, type):
    result = zip(*context)
    result_list = list(result)
    sum_char = 0
    if type == 'twitter':
        for i in result_list[1]:
            sum_char += len(i)
    if type == 'pubmed':
        for i in result_list[0]:
            sum_char += len(i)
        for i in result_list[1]:
            sum_char += len(i)

    return sum_char


def count_string_of_word(context, type):
    result = zip(*context)
    result_list = list(result)
    sum_word = 0
    if type == 'twitter':
        for i in result_list[1]:
            sum_word += len(i.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).split())
    if type == 'pubmed':
        for i in result_list[0]:
            sum_word += len(i.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).split())
        for i in result_list[1]:
            sum_word += len(i.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).split())

    return sum_word


def cutting_sentence_of_dot(sentence):
    length = 20
    cutting_result_list = list()
    for idx in range(length, len(sentence) - length):
        if sentence[idx] == ".":
            cutting_result_list.append(sentence[idx - length:idx + length])
    return cutting_result_list


def model_predict_end_of_sentence(processed_text_list):
    model = load_model('eos_model.h5')
    token = Tokenizer(filters='', char_level=True)
    token.fit_on_texts(processed_text_list)
    list_seq = token.texts_to_sequences(processed_text_list)
    list_seq_with_padding = sequence.pad_sequences(list_seq, maxlen=40)
    predict_result = model.predict_classes(list_seq_with_padding).reshape(-1)
    backend.clear_session()
    return predict_result


def count_string_of_sentence(context, type):
    result = zip(*context)
    result_list = list(result)
    sum_sentence = 0
    if type == 'twitter':
        for i in result_list[1]:
            processed_text_list = cutting_sentence_of_dot(i)
            if len(processed_text_list) == 0:
                sum_sentence += 1
            else:
                predict_result = model_predict_end_of_sentence(processed_text_list)
                sum_sentence += np.count_nonzero(predict_result == 1)

    if type == 'pubmed':
        for i in result_list[1]:
            processed_text_list = cutting_sentence_of_dot(i)
            if len(processed_text_list) == 0:
                sum_sentence += 1
            else:
                predict_result = model_predict_end_of_sentence(processed_text_list)
                sum_sentence += np.count_nonzero(predict_result == 1)

    return sum_sentence


def add_keyword_dict(context, type, keyword_dict, title_collection, context_collection):
    result = zip(*context)
    result_list = list(result)

    if type == 'twitter':
        for idx, val in enumerate(result_list[1]):
            context_collection.append(val)
            title_collection.append(result_list[0][idx])
            word_split = val.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).lower().split()
            for word in word_split:
                if not word.isdigit():
                    keyword_map = keyword_dict.get(word, list())
                    keyword_map.append(len(context_collection) - 1)
                    keyword_dict[word] = keyword_map
    if type == 'pubmed':
        for val in context:
            title_collection.append(val[0])
            context_collection.append(val[1])
            title_word_split = val[0].translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).lower().split()
            context_word_split = val[1].translate(
                {ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).lower().split()
            for word in title_word_split:
                if not word.isdigit():
                    keyword_map = keyword_dict.get(word, list())
                    keyword_map.append(len(context_collection) - 1)
                    keyword_dict[word] = keyword_map
            for word in context_word_split:
                if not word.isdigit():
                    keyword_map = keyword_dict.get(word, list())
                    keyword_map.append(len(context_collection) - 1)
                    keyword_dict[word] = keyword_map

    return keyword_dict, title_collection, context_collection


def look_up_keyword(lookup_dict, title_context_pair, keyword_to_search):
    result_list = list()
    if keyword_to_search != '':
        match_index = lookup_dict.get(keyword_to_search, -1)
        if match_index == -1:
            return result_list
        # handle same word repeat index
        for each_index in list(set(match_index)):
            result_list.append(title_context_pair[each_index])
        return result_list
    else:
        return result_list
