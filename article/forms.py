from django.forms import ModelForm, TextInput, Select
from .models import Article, Comment


# Text Create Form.

class CreateTextForm(ModelForm):

    class Meta:
        model = Article

        exclude = ["like", "view"]


        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }


# Comment Create Form.

class CommentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

        self.fields['text'].widget.attrs['rows'] = 10
        self.fields['text'].widget.attrs['cols'] = 150
        self.fields['text'].widget.attrs['placeholder'] = 'Write your  comment here...'

    class Meta:

        model = Comment
        fields = ('author', 'text')
