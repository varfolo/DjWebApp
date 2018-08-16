from django.contrib.auth.models import User
from django import forms 


class ProductApplyForm(forms.Form):
    userId = forms.CharField()
    productName = forms.CharField(max_length=50)
    description = forms.CharField(max_length=2000,
                                   widget=forms.Textarea)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    category = forms.CharField(max_length=20)
    image = forms.FileField()
    #CreateDate = forms.DateTimeField()

class UserForm(forms.ModelForm):
        password = forms.CharField(widget = forms.PasswordInput, label="Пароль")

        class Meta:
            model = User
            fields = ['username', 'email', 'password']
            labels = { 
                'username': 'Имя', 'email': 'Адрес электронной почты', 'password': 'Пароль'
                }

                        