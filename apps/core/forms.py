from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Your Username",
        required=True,
        widget=forms.TextInput(
            attrs = { "class": "form-control" }
        )
    )
    password = forms.CharField(
        label="Your Password",
        required=True,
        widget=forms.PasswordInput(
            attrs = { "class": "form-control" }
        )
    )


