from django import forms

class StudentRegestrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()