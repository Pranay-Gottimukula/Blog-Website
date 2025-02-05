from django import forms
from .models import PostModel

# Making a form for posts
class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')

# Making a form for updating post
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')