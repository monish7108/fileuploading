from django import forms
from .models import cust_details
class registrationForm(forms.ModelForm):
    cust_account_id = forms.IntegerField()
    cust_name = forms.CharField()
    cust_address = forms.Textarea()
    cust_dob = forms.DateField()
    cust_email = forms.EmailField()
    cust_balance = forms.IntegerField()

    class Meta:
        model = cust_details
        fields="__all__"