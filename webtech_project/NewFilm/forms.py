from django import forms
from .models import Post

class CommentForm(forms.Form):
    title = forms.CharField(max_length=90)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=90)
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    active = forms.ChoiceField(required=False, widget=forms.CheckboxInput)
    
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'date', 'active']