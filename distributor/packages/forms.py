from django import forms


class PackageUploadForm(forms.Form):
    package = forms.FileField()
    channel = forms.CharField(max_length=255)
    branch = forms.CharField(max_length=255)


class DebugSymbolsUploadForm(forms.Form):
    debug_symbols = forms.FileField()
 
