from django import forms
from .models import Account,Transfer

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['from_account','to_account','amount']
