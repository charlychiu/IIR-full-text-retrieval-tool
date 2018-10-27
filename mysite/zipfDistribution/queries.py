def get_content_is_raw_by_document(document):
    return document.contents.all().filter(is_raw=True)


def get_content_not_raw_by_document(document):
    return document.contents.all().filter(is_raw=False)
