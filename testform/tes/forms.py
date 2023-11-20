from django import forms

class smart_Form(forms.Form):
    title = forms.CharField(max_length=255)
    image = forms.ImageField()
    body = forms.CharField(widget= forms.Textarea)
