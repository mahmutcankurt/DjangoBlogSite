from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if '@' in username:
            user = User.objects.filter(email=username)
            if len(user) == 1:
                user = user.first()
                return user.username
            elif len(user) > 1:
                raise forms.ValidationError('Please enter your username !')
            else:
                raise forms.ValidationError('There is no user in our list !')
        return username
