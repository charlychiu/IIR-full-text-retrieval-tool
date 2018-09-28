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
    # words = context.split()
    # return len(words)
    return 0


def count_string_of_sentence(context, type):
    # running model
    return 0  # number of sentence

# def create_word_dict()
