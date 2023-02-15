from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = ''
            self.fields[field].label = ''
        self.fields['first_name'].widget.attrs.update({'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last Name'})
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password'})

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.firstname = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user
    
class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = ''
            self.fields[field].label = ''
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'placeholder':'Password'})


class UpdateForm(forms.Form):
    change = forms.IntegerField(max_value=999, label='',required=False, widget= forms.NumberInput(attrs={
                                'placeholder':'Add/Remove products', 'required': 'True' }))