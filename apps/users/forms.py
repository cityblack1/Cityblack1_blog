from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.core.exceptions import *

from wagtail.wagtailusers.forms import UserEditForm, UserCreationForm

from .models import User
from api.views import check_from_db



class CustomUserEditForm(UserEditForm):
    cover_image = forms.ImageField(required=False, label=_('头像'))


class CustomUserCreationForm(UserCreationForm):
    cover_image = forms.ImageField(required=False, label=_('头像'))


class CustomAuthenticationBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
        except:
            raise PermissionDenied
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=128)
    password2 = forms.CharField(max_length=128, required=True)

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) > 20 or len(data) < 4:
            msg = '用户名长度只能在4-20位字符之间'
            raise forms.ValidationError(msg)
        if check_from_db(data):
            msg = '用户名已经存在'
            raise forms.ValidationError(msg)
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if check_from_db(data, 'email'):
            msg = '该邮箱已被使用，请重新输入'
            raise forms.ValidationError(msg)
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) > 16 or len(data) < 6:
            msg = '密码长度只能在6-20位字符之间'
            raise forms.ValidationError(msg)
        return data

    def clean_password2(self):
        data = self.cleaned_data['password2']
        if len(data) > 16 or len(data) < 6:
            msg = '密码长度只能在6-20位字符之间'
            raise forms.ValidationError(msg)
        return data

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                msg = '两次输入密码不一致'
                self.add_error('password', msg)
                self.add_error('password2', msg)
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'email']