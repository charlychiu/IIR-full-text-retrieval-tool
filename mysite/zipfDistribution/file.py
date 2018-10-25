from os import listdir, path, remove
from os.path import isfile, join
from .json_reader import twitter_json_parser
from .xml_reader import pubmed_xml_parser
import hashlib


def get_file_path(file_name):
    return 'upload/' + file_name


def read_file_in_upload_folder():
    return [f for f in listdir('upload') if isfile(join('upload', f)) if f != '.gitignore']


def file_set_generate_md5_checksum(file_list):
    hash_obj = hashlib.md5(open(get_file_path(file_list[0]), 'rb').read())
    if len(file_list) > 1:
        for filename in file_list[1:]:
            hash_obj.update(open(get_file_path(filename), 'rb').read())
    checksum = hash_obj.hexdigest()
    return checksum


def get_documents_from_file_set(file_list):
    result_list = list()
    for file in file_list:
        if ".json" in file.lower():
            get_result = twitter_json_parser(get_file_path(file))
            result_list.extend(get_result)
        elif ".xml" in file.lower():
            get_result = pubmed_xml_parser(get_file_path(file))
            result_list.extend(get_result)
        else:
            print('Error file type detect')
    return result_list
