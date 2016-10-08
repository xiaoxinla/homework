from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='username', max_length = 50)
    password1 = forms.CharField(label='password', max_length = 50)
    password2 = forms.CharField(label='configure',max_length = 50)
    phone = forms.CharField(label='phone', max_length = 50)


class UserLoginForm(forms.Form):
    name = forms.CharField(label='username', max_length = 50)
    password = forms.CharField(label = 'password', max_length = 50)
