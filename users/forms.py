from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', )


class UserProfile(forms.ModelForm):
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'
    GENDER = ((MALE, 'Male'), (FEMALE, 'Female'), (UNDEFINED, 'Undefined'))

    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    bio = forms.CharField(widget=forms.Textarea, max_length=500, label='Bio')
    birth_date = forms.DateField(widget=forms.SelectDateWidget, label='Birth Date')
    phone_number = forms.CharField(max_length=11, label='Phone Number')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'phone_number', 'gender', 'bio']

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


#class UserProfileEdit(forms.ModelForm):
    #class Meta:
        #model = Profile
        #fields = ['gender', 'phone_number', 'birth_date', 'bio']


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
