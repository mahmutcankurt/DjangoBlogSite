from django.forms import ModelForm, Textarea
from .models import Article

#from captcha.fields import ReCaptchaField


class CreateTextForm(ModelForm):

    class Meta:
        model = Article

        exclude = ["like", "view"]

        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'textClass'})
        }
