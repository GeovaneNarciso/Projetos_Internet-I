from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'tag',)
        widgets = {'text': forms.Textarea(attrs={'type': 'textarea'})}

    def clean_tag(self):
        tag = self.cleaned_data['tag']
        if '#' not in tag:
            raise forms.ValidationError("Place # at the beginning of the tag.")
        return tag

    '''def clean_tag(self):
        tag = self.cleaned_data['tag']
        if '#' not in tag:
            msg = "Place # at the beginning of the tag."
            self.add_error('tag', msg)
        return tag'''
