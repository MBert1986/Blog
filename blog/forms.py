from django import forms

from .models import Post

class PostCreatForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content')