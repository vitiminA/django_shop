from django import forms
from .models import postModel
class post_Model(forms.ModelForm):
    class Meta:
        model = postModel
        fields = ['title', 'image', 'body']
