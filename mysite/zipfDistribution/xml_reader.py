import xml.etree.ElementTree as ET
import os.path
import re


# For handing special tag, like HTML element in XML tag => cause error
def handle_special_tag(file_path):
    input_file = open(file_path, encoding="utf-8")
    xml_contents = input_file.read()
    input_file.close()
    # Avoid to override original file, create backup one
    output_file = open(file_path + "-backup", "w", encoding="utf-8")
    output_file.write(xml_contents)
    output_file.close()
    # Replace tag with space
    xml_contents = re.sub('<sup>.*?</sup>', ' ', xml_contents)
    xml_contents = re.sub('<i>.*?</i>', ' ', xml_contents)
    # Save modify one
    output_file = open(file_path, "w", encoding="utf-8")
    output_file.write(xml_contents)
    output_file.close()


def read_xml_file(file_path):
    if os.path.isfile(file_path):
        # handle_special_tag(file_path)
        get_xml_tree = ET.parse(file_path)
        print("xml-reader: Detect root element tag: {}".format(get_xml_tree.getroot().tag))
        return get_xml_tree
    else:
        print("xml-reader: Read file error (file not exist)")
        return


def full_text_search_in_xml(xml_tree, *args):
    """
        Leave args empty -> retrieval all type
        Accept args : PubmedBookArticle, PubmedArticle
    """
    documents = xml_tree.getroot()
    collection_list = list()
    if ET.iselement(documents):
        count_of_document = len(documents)
        print("xml-reader: total documents: {}".format(str(count_of_document)))
        print("xml-reader: correctly set")

        if args:
            for arg in args:
                if arg == 'PubmedBookArticle':
                    print('xml-reader: arg. PubmedBookArticle')
                    collection_list.extend(retrieval_pubmed_book_article(documents))
                if arg == 'PubmedArticle':
                    print('xml-reader: arg. PubmedArticle')
                    collection_list.extend(retrieval_pubmed_article(documents))
                else:
                    print('xml-reader: arg. error')
        else:
            print('xml-reader: arg. PubmedBookArticle & PubmedArticle')
            collection_list.extend(retrieval_pubmed_book_article(documents))
            collection_list.extend(retrieval_pubmed_article(documents))

        return collection_list
    else:
        print("xml-reader: setting fail")
        return list()


def retrieval_pubmed_book_article(documents):
    collection_list = list()
    ''' PubmedBookArticle type data'''
    for child_of_root in documents.iterfind('PubmedBookArticle/BookDocument'):
        tmp_list = list()
        # print(child_of_root.find('ArticleTitle').text)
        try:
            tmp_list.append(child_of_root.find('ArticleTitle').text)  ## ArticleTitle
        except:
            pass
        # try:
        #     tmp_list.append(child_of_root.find('Book/BookTitle').text)  ## Book/BookTitle
        # except:
        #     pass

        # print(child_of_root.find('Abstract/AbstractText'))
        tmp_list.append(child_of_root.find('Abstract/AbstractText').text)  ## AbstractText
        collection_list.append(tmp_list)

    # for child_of_root in documents.iterfind('PubmedBookArticle/BookDocument/ArticleTitle'):
    #     print("tag: {}, text: {}".format(child_of_root.tag, child_of_root.text))
    # for child_of_root in documents.iterfind('PubmedBookArticle/BookDocument/Abstract/AbstractText'):
    #     print("tag: {}, text: {}".format(child_of_root.tag, child_of_root.text))
    return collection_list


def retrieval_pubmed_article(documents):
    collection_list = []
    ''' PubmedArticle type data'''
    for child_of_root in documents.iterfind('PubmedArticle/MedlineCitation/Article'):
        tmp_list = list()
        # print(child_of_root.find('ArticleTitle').text)
        tmp_list.append(child_of_root.find('ArticleTitle').text)  ## ArticleTitle
        # print(child_of_root.findall('Abstract/AbstractText'))  ## Abstract

        abstract_texts = child_of_root.findall('Abstract/AbstractText')
        tmp_str = ''
        for abstract_text in abstract_texts:
            try:
                tmp_str += abstract_text.text + ' '
            except:
                pass
        # print(tmp_str)
        tmp_list.append(tmp_str)
        collection_list.append(tmp_list)
    return collection_list


def pubmed_xml_parser(file_path, *args):
    get_tree = read_xml_file(file_path)
    parse_result = full_text_search_in_xml(get_tree, *args)
    return parse_result


if __name__ == "__main__":
    #     # For debug use
    #     # print("xml-reader: error usage")
    #     # result = pubmed_xml_parser('./pubmed_result.xml', 'PubmedBookArticle')
    result = pubmed_xml_parser('../upload/pubmed_result_ebola.xml')
    print(result)
    print(len(result))
#
#     print("!!")
#     print(len(result))
#     # print(get_result[0])
#     # print(get_result[1])
#     # print(get_result[2])
