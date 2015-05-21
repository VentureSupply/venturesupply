from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Business Name', max_length=50)
