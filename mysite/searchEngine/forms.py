from django import forms


class UploadFileForm(forms.Form):
    file_input = forms.FileField()
