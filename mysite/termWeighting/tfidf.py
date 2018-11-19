from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk import sent_tokenize


def combine_title_and_abstract(documents):
    result_collection = list()
    for doc in documents:
        result_collection.append(doc[0] + doc[1])
    return result_collection


def tfidf_with_norm(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    result_collection = list()
    for i in range(len(weight)):
        tmp_collection = list()
        for j in range(len(word)):
            if weight[i][j] != 0.0:
                tmp_collection.append([word[j], weight[i][j]])
        tmp_collection.sort(key=lambda x: x[1], reverse=True)
        result_collection.append(tmp_collection[:7])
        # print(word[j], weight[i][j])
    return result_collection


def tfidf_without_norm(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer(norm=None)
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    result_collection = list()
    for i in range(len(weight)):
        tmp_collection = list()
        for j in range(len(word)):
            if weight[i][j] != 0.0:
                tmp_collection.append([word[j], weight[i][j]])
        tmp_collection.sort(key=lambda x: x[1], reverse=True)
        result_collection.append(tmp_collection[:7])
    return result_collection


def tfidf_with_sublinear(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer(sublinear_tf=True)
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    result_collection = list()
    for i in range(len(weight)):
        tmp_collection = list()
        for j in range(len(word)):
            if weight[i][j] != 0.0:
                tmp_collection.append([word[j], weight[i][j]])
        tmp_collection.sort(key=lambda x: x[1], reverse=True)
        result_collection.append(tmp_collection[:7])
    return result_collection


def cut_document_to_sentence(document):
    sent_tokenize_list = sent_tokenize(document)
    return sent_tokenize_list


def cut_document_set_to_sentence(document_set):
    result_collection = list()
    for doc in document_set:
        result_collection.extend(cut_document_to_sentence(doc))
        # tmp_collection = list()
        # tmp_collection.extend(cut_document_to_sentence(content))
        # result_collection.append(tmp_collection)
    return result_collection


def keyword_search_for_tfidf_ranking(corpus, keyword):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer(sublinear_tf=True)
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    result_collection = list()
    for i in range(len(weight)):
        tmp_collection = list()
        for j in range(len(word)):
            if weight[i][j] != 0.0 and word[j] == keyword:
                tmp_collection.extend([i, weight[i][j]])
            elif weight[i][j] == 0.0 and word[j] == keyword:
                tmp_collection.extend([i, -1])
        # tmp_collection.sort(key=lambda x: x, reverse=True)
        result_collection.append(tmp_collection)
    return result_collection


if __name__ == "__main__":
    corpus = ['Vaccine (Vaccination)',
              'Immunization is a successful use of immunotherapy to treat many infectious diseases by stimulating the immune system to produce specific antibodies or specific lymphocytes to fight off pathogens and more recent to protect against malignant tumors.\xa0 This immunotherapy creates an immunological memory that can be long-lasting. The current immunizations protect against diphtheria, tetanus, pertussis, poliomyelitis, measles, mumps, rubella, pneumococcal pneumonia, smallpox, sepsis, meningitis, hepatitis B, varicella-zoster, tuberculosis, cholera, diarrhea caused by rotavirus, salmonellosis, and dengue. However, the development of vaccine technology in recent years, the emergence of HIV, SARS, avian influenza, Ebola, and Zika emphasizes the need for global preparedness for a pandemic.[1].\xa0']
    # tfidf_with_norm(corpus=coupus)
    # tfidf_without_norm(corpus=coupus)
    # tfidf_with_sublinear(corpus=coupus)
    # cut_document_to_sentence(coupus[1])
    # result = cut_document_set_to_sentence([corpus])
    # print(result)
    test = keyword_search_for_tfidf_ranking(corpus, 'the')
    print(test)
