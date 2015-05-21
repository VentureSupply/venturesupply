from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Business Name', max_length=50)

class CertForm(forms.Form):
    certificate = forms.CharField(label='Certificate', max_length=15)
