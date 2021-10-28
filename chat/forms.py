from allauth.account.forms import SignupForm
from django import forms
from django.forms import ModelForm
from chat.models import User

#SEX_CHOICES = (('M', 'Мужчина'), ('W', 'Женщина'), ('N', 'Неопределенный'))


#class MySignUpForm(SignupForm):
    #age = forms.IntegerField(label='id_age', required=True,
                             #widget=forms.TextInput(
                                 #attrs={"type": "number", "placeholder": "Возраст", "min": "1"}
                             #))
    #sex = forms.CharField(label='id_sex', required=True, widget=forms.Select(choices=SEX_CHOICES))

class CustomSignUpForm(SignupForm):
    about = forms.CharField(label='О себе', required=True, widget=forms.TextInput())

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
