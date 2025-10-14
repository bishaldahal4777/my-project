from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title', 'content','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'class':'form-control','placeholder':'Write a comment...'})
        }
