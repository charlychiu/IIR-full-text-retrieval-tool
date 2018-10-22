from os import listdir, path, remove
from os.path import isfile, join
from .json_reader import twitter_json_parser
from .xml_reader import pubmed_xml_parser
import pickle
import hashlib
from .PorterStemmer import filter_pubmed_data_through_porter


def get_file_path(file_name):
    return 'upload/' + file_name


def read_file_in_upload_folder():
    return [f for f in listdir('upload') if isfile(join('upload', f)) if f != '.gitignore']


def file_list_with_md5(file_list):
    hash_obj = hashlib.md5(open(get_file_path(file_list[0]), 'rb').read())
    if len(file_list) > 1:
        for fname in file_list[1:]:
            hash_obj.update(open(get_file_path(fname), 'rb').read())
    checksum = hash_obj.hexdigest()
    return checksum


def get_porter_result(file_list):
    for file in file_list:
        if ".json" in file.lower():
            # get_file = twitter_json_parser(get_file_path(file))
            pass
        elif ".xml" in file.lower():
            get_file = pubmed_xml_parser(get_file_path(file))
            # result = filter_pubmed_data_through_porter(get_file)
            return get_file
            pass
        else:
            pass
