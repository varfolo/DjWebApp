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
        password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), label="Пароль")
        password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), label="Пароль")
        userPic = forms.FileField()
#        email = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control'}), label="Адрес электронной почты")

        class Meta:
            model = User
            fields = ['username', 'email', 'password', 'password2', 'userPic']
            labels = { 
                'username': 'Имя', 'email': 'Адрес электронной почты', 'password': 'Пароль', 'password2': 'Повторный пароль', 'userPic': 'Аватар пользователя'
                }
 
        def clean_username(self):
            username = self.cleaned_data['username']
                    #if User.objects.exclude(pk=user.instace.pk).filter(username=username).exists():
            #if "waw" == username:
            #if User.objects.exclude(pk=self.instace.pk).filter(username=username).exists():
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("К сожалению, пользователь с таким именем уже зарегистрирован в системе")
            return username    

        def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("К сожалению, пользователь с такой электронной почтой уже зарегистрирован в системе")
            return email 
