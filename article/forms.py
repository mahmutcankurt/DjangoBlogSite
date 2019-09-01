from django.forms import ModelForm, TextInput, Select
from .models import Article

#from captcha.fields import ReCaptchaField


class CreateTextForm(ModelForm):

    class Meta:
        model = Article

        exclude = ["like", "view"]


        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }
