from django.contrib.auth import forms as auth_forms
from django import forms

from BlogAPP.authentication.models import Profile
from common import form_mixins


class SignUpForm(form_mixins.BoostrapMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


class SignInForm(form_mixins.BoostrapMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture',)
