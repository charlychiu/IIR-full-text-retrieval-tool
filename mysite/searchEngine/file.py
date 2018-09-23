from os import listdir
from os.path import isfile, join


def save_file_from_post(file):
    with open('upload/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def read_file_in_upload_folder():
    return [f for f in listdir('upload') if isfile(join('upload', f))]

