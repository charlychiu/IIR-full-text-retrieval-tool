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


def count_string_of_sentence(context, type):
    # running model
    return 0  # number of sentence


def add_keyword_dict(context, type, keyword_dict, title_collection, context_collection):
    result = zip(*context)
    result_list = list(result)

    if type == 'twitter':
        for idx, val in enumerate(result_list[1]):
            context_collection.append(val)
            title_collection.append(result_list[0][idx])
            word_split = val.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).split()
            for word in word_split:
                if not word.isdigit():
                    keyword_map = keyword_dict.get(word, list())
                    keyword_map.append(len(context_collection) - 1)
                    keyword_dict[word] = keyword_map
    if type == 'pubmed':
        # for i in result_list[0]:
        #     sum_word += len(i.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).split())
        # for i in result_list[1]:
        #     sum_word += len(i.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).split())
        pass

    return keyword_dict, title_collection, context_collection
