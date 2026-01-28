from django import forms
from core.models import *



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text':forms.Textarea(attrs={'class':'comment-input','rows':'5','placeholder':'Message'})
        }