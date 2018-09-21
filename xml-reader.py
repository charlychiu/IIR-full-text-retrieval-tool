import xml.etree.ElementTree as ET
import os.path


def read_xml_file(file_path):
    if os.path.isfile(file_path):
        get_xml_tree = ET.parse(file_path)
        print("xml-reader: Detect root element tag: {}".format(get_xml_tree.getroot().tag))
        return loading_from_xml(xml_tree=get_xml_tree)
    else:
        print("xml-reader: Read file error (file not exist)")
        return


def loading_from_xml(xml_tree):
    documents = xml_tree.getroot()
    count_of_document = len(documents)
    collection_list = []
    if ET.iselement(documents):
        print("correctly set")
        print(count_of_document)
        document = documents.iter()
        tmp_list = []
        for child in document:
            # child.tag child.attrib child.text
            # if child.tag == "PubmedBookArticle" or child.tag == "PubmedBookArticle":
            if len(tmp_list) == 2:
                collection_list.append(tmp_list)
                tmp_list = []
            if child.tag == "ArticleTitle":
                print("article title: {}".format(child.text))
                tmp_list.append(child.text)
            if child.tag == "AbstractText":
                print("abstract text: {}".format(child.text))
                tmp_list.append(child.text)
        return collection_list
    else:
        print("setting fail")
        return list()


if __name__ == "__main__":
    # For debug use
    # print("error usage")
    get_result = read_xml_file('./pubmed_result.xml')
    print("!!")
    print(len(get_result))
    print(get_result[0])
    print(get_result[1])
    print(get_result[2])
