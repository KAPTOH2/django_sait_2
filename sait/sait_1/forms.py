from django import forms
from .models import AbcModel
from django.forms import ModelForm

class StudentForm(forms.Form):
    names = forms.CharField(label="Имена учеников", widget=forms.Textarea(attrs={'rows': 4}))
    grades = forms.CharField(label="Оценки", widget=forms.Textarea(attrs={'rows': 4}))

class AbcModelForm(ModelForm):
    # task = forms.CharField(widget=forms.Textarea({'cols': '60', 'rows': "3"}))
    # task.widget.attrs.update({'cols': '40', 'rows': "2"})
    class Meta:
        model = AbcModel
        fields = '__all__'
        # fields = ['task', 'a', 'b','c']
        print('\nfields: ', fields)