from os import listdir, path, remove
from os.path import isfile, join
from .text_process import count_string_of_character, count_string_of_word, count_string_of_sentence, add_keyword_dict
from .json_reader import twitter_json_parser
from .xml_reader import pubmed_xml_parser
import pickle
import hashlib


def get_file_path(file_name):
    return 'upload/' + file_name


def save_file_from_post(file):
    with open('upload/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def read_file_in_upload_folder():
    return [f for f in listdir('upload') if isfile(join('upload', f)) if f != '.gitignore']


# def md5_file(file):
#     hash_md5 = hashlib.md5()
#     with open(file, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()


def file_list_with_md5(file_list):
    hash_obj = hashlib.md5(open(get_file_path(file_list[0]), 'rb').read())
    if len(file_list) > 1:
        for fname in file_list[1:]:
            hash_obj.update(open(get_file_path(fname), 'rb').read())
    checksum = hash_obj.hexdigest()
    return checksum


def check_tmp_pkl_exist(file_list):
    name_of_tmp_pkl = file_list_with_md5(file_list)
    if path.exists("tmp/" + str(name_of_tmp_pkl) + ".pkl"):
        return True
    else:
        return False


def load_file_info_from_tmp_pkl(file_list):
    name_of_tmp_pkl = file_list_with_md5(file_list)
    fh = open("tmp/" + str(name_of_tmp_pkl) + ".pkl", 'rb')
    return pickle.load(fh)


def save_file_info_to_tmp_pkl(file_list, data):
    name_of_tmp_pkl = file_list_with_md5(file_list)
    fh = None
    try:
        fh = open("tmp/" + str(name_of_tmp_pkl) + ".pkl", 'wb')
        pickle.dump(data, fh)
    except:
        print("error")
        pass
    finally:
        if fh is not None:
            fh.close()


def clean_tmp_pkl():
    file_list = [f for f in listdir('tmp') if isfile(join('tmp', f))]
    for file_name in file_list:
        if path.exists('tmp/' + file_name) and file_name != ".gitignore":
            remove('tmp/' + file_name)


def clean_upload_file():
    file_list = [f for f in listdir('upload') if isfile(join('upload', f))]
    for file_name in file_list:
        if path.exists('upload/' + file_name) and file_name != ".gitignore":
            remove('upload/' + file_name)


def get_file_info(file_list):  # [[character, word, sentence], dict{}]
    file_info_list = list()
    counting_info_list = list()
    keyword_dict = dict()
    title_collection = list()
    context_collection = list()

    if check_tmp_pkl_exist(file_list):
        file_info_list = load_file_info_from_tmp_pkl(file_list)
        file_info_list.append("load from pkl")
        return file_info_list
    else:
        for file in file_list:
            if ".json" in file.lower():
                get_file = twitter_json_parser(get_file_path(file))
                counting_info_list.append(
                    [count_string_of_character(get_file, 'twitter'), count_string_of_word(get_file, 'twitter'),
                     count_string_of_sentence(get_file, 'twitter')])
                keyword_dict, title_collection, context_collection = add_keyword_dict(get_file, 'twitter', keyword_dict,
                                                                                      title_collection,
                                                                                      context_collection)

            elif ".xml" in file.lower():
                get_file = pubmed_xml_parser(get_file_path(file))
                counting_info_list.append(
                    [count_string_of_character(get_file, 'pubmed'), count_string_of_word(get_file, 'pubmed'),
                     count_string_of_sentence(get_file, 'pubmed')])
                keyword_dict, title_collection, context_collection = add_keyword_dict(get_file, 'pubmed', keyword_dict,
                                                                                      title_collection,
                                                                                      context_collection)
            else:
                counting_info_list.append("QQ")

        file_info_list.append(counting_info_list)
        file_info_list.append(keyword_dict)
        file_info_list.append(list(zip(title_collection, context_collection)))
        save_file_info_to_tmp_pkl(file_list, file_info_list)
        file_info_list.append("save to pkl")

        return file_info_list
