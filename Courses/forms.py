from django import forms

class LoginForm(forms.Form):
    name     = forms.CharField(widget=forms.TextInput(attrs={"autocomplete":"off" ,
                                                        "type":"text" ,
                                                         "name" :"log_username" ,
                                                           "class":"required form-control"  ,
                                                           "placeholder":"Email Address",
                                                            "style":" margin-bottom: 10px;"}) , label='')

    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete":"off" ,
                                                        "type":"password" ,
                                                         "name" :"log_password" ,
                                                         "class":"password required form-control"  ,
                                                         "placeholder":"Password" ,
                                                         "style":" margin-bottom: 19px;"}) , label='')
