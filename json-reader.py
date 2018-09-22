import json
from pprint import pprint


def read_json_file(file_path):
    with open(file_path, encoding='utf8') as f:
        data = json.load(f)
    # pprint(data)
    return data


def data_handling(data):
    collection_list = []
    for msg in data:
        tmp_list = list()
        tmp_list.append(msg['id'])
        tmp_list.append(msg['text'])
        collection_list.append(tmp_list)
    return collection_list


def twitter_json_parser(file_path):
    get_raw_data = read_json_file(file_path)
    parse_result = data_handling(get_raw_data)
    return parse_result


if __name__ == "__main__":
    # read_json_file('./Tweet_Json.json')
    result = twitter_json_parser('./twitter_3.json')
    result = zip(*result)
    print(list(result))
    # print(result[0]['id'])
    # print(result[0]['text'])
