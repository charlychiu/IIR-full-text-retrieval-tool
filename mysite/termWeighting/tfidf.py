from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


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
            tmp_collection.append([word[j], weight[i][j]])
        result_collection.append(tmp_collection)
            # print(word[j], weight[i][j])
    return result_collection

def tfidf_without_norm(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer(norm=None)
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    for i in range(len(weight)):
        for j in range(len(word)):
            print(word[j], weight[i][j])


def tfidf_with_sublinear(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer(sublinear_tf=True)
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    for i in range(len(weight)):
        for j in range(len(word)):
            print(word[j], weight[i][j])


if __name__ == "__main__":
    coupus = ['Vaccine (Vaccination)',
              'Immunization is a successful use of immunotherapy to treat many infectious diseases by stimulating the immune system to produce specific antibodies or specific lymphocytes to fight off pathogens and more recent to protect against malignant tumors.\xa0 This immunotherapy creates an immunological memory that can be long-lasting. The current immunizations protect against diphtheria, tetanus, pertussis, poliomyelitis, measles, mumps, rubella, pneumococcal pneumonia, smallpox, sepsis, meningitis, hepatitis B, varicella-zoster, tuberculosis, cholera, diarrhea caused by rotavirus, salmonellosis, and dengue. However, the development of vaccine technology in recent years, the emergence of HIV, SARS, avian influenza, Ebola, and Zika emphasizes the need for global preparedness for a pandemic.[1].\xa0']
    tfidf_with_norm(corpus=coupus)
    tfidf_without_norm(corpus=coupus)
    tfidf_with_sublinear(corpus=coupus)
