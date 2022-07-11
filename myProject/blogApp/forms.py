from django import forms
from blogApp import models

class PostForm(forms.ModelForm):

    class Meta():
        model = models.Post
        ## Previously Used
        # fields = ('title', 'content', 'author')

        ## Now Used
        fields = ('title','content')

class CommentForm(forms.ModelForm):

    class Meta():
        model = models.Comment
        ## Previously Used
        #fields = ('text', 'author', 'post')

        ## Now Used
        fields = ('text', )