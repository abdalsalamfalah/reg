from django import forms
from salam import models
class inforeg(forms.Form):
    Full_name=forms.CharField(required=True,widget=forms.TextInput(),label='اسم المريض')
    The_age=forms.CharField(required=True,widget=forms.TextInput(),label='العمـــر')
    Phone_num=forms.CharField(required=True,widget=forms.TextInput(),label='رقــم الهـاتف')
    
    
class updateinfo(forms.ModelForm):
    class Meta:
        model=models.info
        fields=['full_name','the_age','phone_number']
    
