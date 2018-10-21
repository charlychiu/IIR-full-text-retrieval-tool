from .json_reader import twitter_json_parser
from .xml_reader import pubmed_xml_parser

def get_file_path(file_name):
    return 'upload/' + file_name


def get_file_info(file_list):
    for file in file_list:
        if ".json" in file.lower():
            get_file = twitter_json_parser(get_file_path(file))
            pass
        elif ".xml" in file.lower():
            get_file = pubmed_xml_parser(get_file_path(file))
            pass
        else:
            pass
    pass
