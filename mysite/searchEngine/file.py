from os import listdir
from os.path import isfile, join
from .text_process import count_string_of_character, count_string_of_word, count_string_of_sentence, add_keyword_dict
from .json_reader import twitter_json_parser
from .xml_reader import pubmed_xml_parser


def get_file_path(file_name):
    return 'upload/' + file_name


def save_file_from_post(file):
    with open('upload/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def read_file_in_upload_folder():
    return [f for f in listdir('upload') if isfile(join('upload', f))]


def get_file_info(file_list):  # [[character, word, sentence], dict{}]
    file_info_list = list()
    keyword_dict = dict()
    context_collection = list()
    for file in file_list:
        if ".json" in file.lower():
            get_file = twitter_json_parser(get_file_path(file))
            file_info_list.append(
                [count_string_of_character(get_file, 'twitter'), count_string_of_word(get_file, 'twitter'),
                 count_string_of_sentence(get_file, 'twitter')])
            keyword_dict, context_collection = add_keyword_dict(get_file, 'twitter', keyword_dict, context_collection)

        elif ".xml" in file.lower():
            get_file = pubmed_xml_parser(get_file_path(file))
            file_info_list.append(
                [count_string_of_character(get_file, 'pubmed'), count_string_of_word(get_file, 'pubmed'),
                 count_string_of_sentence(get_file, 'pubmed')])
        else:
            file_info_list.append("QQ")

    file_info_list.append(keyword_dict)
    file_info_list.append(context_collection)
    return file_info_list
