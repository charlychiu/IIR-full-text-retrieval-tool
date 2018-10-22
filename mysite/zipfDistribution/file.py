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


def get_porter_result(file_list):
    for file in file_list:
        if ".json" in file.lower():
            # get_file = twitter_json_parser(get_file_path(file))
            pass
        elif ".xml" in file.lower():
            get_file = pubmed_xml_parser(get_file_path(file))
            result = filter_pubmed_data_through_porter(get_file)
            return result
            pass
        else:
            pass