from django import forms
from django.contrib.auth import get_user_model 


User=get_user_model()


class sign(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), min_length=1)
    confirmPassword = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    def clean(self):
        password = self.cleaned_data.get('password')
        confirmPassword = self.cleaned_data.get('confirmPassword')
        username= self.cleaned_data.get('username')
        email= self.cleaned_data.get('email')
        
        useremail=User.objects.filter(email__iexact=email)
        if not useremail.exists():
            raise forms.ValidationError("you already have an account,try login")

        
        usern=User.objects.filter(username__iexact=username)
        if not usern.exists():
            raise forms.ValidationError("username  taken")
        
        if password and password != confirmPassword:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data



class log(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), min_length=1)

    def clean_username(self):
        username= self.cleaned_data.get('username')
        qs=User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user")
        return username


 