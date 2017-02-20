from django import forms
from .models import cust_details

class registrationForm(forms.ModelForm):
    class Meta:
        model=cust_details
        fields="__all__"
    # cust_account_id = forms.IntegerField()
    # cust_name = forms.CharField()
    # cust_address = forms.Textarea()
    # cust_dob = forms.DateField()
    # cust_email = forms.EmailField()
    # cust_balance = forms.IntegerField()
    # cust_image=forms.ImageField("pictures/")
    # # class Meta:
    #     model = cust_details
    #     fields="__all__"