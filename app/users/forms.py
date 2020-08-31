from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText
from crispy_forms.layout import (Submit, 
                                Layout, 
                                Fieldset, 
                                Row, 
                                Column, 
                                Field,
                                ButtonHolder,
                                Div,
)

from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={'required': ('Email field "@" required')})
    
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    
    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('username', css_class='col-md-10 form-group form-control m-2', placeholder='username'),
            Field('email', css_class='col-md-10 form-group form-control m-2', placeholder='email'),
            Field('password1', css_class='col-md-10 form-group form-control m-2', placeholder='password'),
            Field('password2', css_class='col-md-10 form-group form-control m-2', placeholder='confirm password'),

            ButtonHolder(
                Submit(
                    'submit', 'Reg User', css_class='col-sm-4 offset-sm-2 m-2', **kwargs
                )
            )
        )
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
    
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserLoginForm(AuthenticationForm):
    username = UsernameField(label='Username', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',}),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
    
    def __init__(self,request=None, *args, **kwargs):
        self.request = request
        self.helper = FormHelper()

        self.helper.form_class = 'form-vertical'
        self.helper.form_method = 'post'
        # self.helper.field_class = 'col-4 m-3'
        self.helper.label_class = 'col-sm-4 text-warning'

        self.helper.layout = Layout(
            Fieldset('Username'),
            Field('username', css_class='col-md-10 form-group form-control m-2'),
            Fieldset('Password'),
            Field('password', css_class='col-md-10 form-group form-control m-2'),
        )

        self.helper.add_input(
            Submit(
                'submit', 'Log In', css_class='col-sm-4 offset-sm-2 m-2', **kwargs
            )
        )


        super(UserLoginForm, self).__init__(*args, **kwargs)