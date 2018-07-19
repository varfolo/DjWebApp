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