from django.forms.models import ModelForm

from .models import Contact


from django import forms
from django.utils.translation import ugettext_lazy as _

from django_comments_xtd.forms import XtdCommentForm


class MyCommentForm(XtdCommentForm):
    qq_num = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('qq_num')})
    )

    def get_comment_create_data(self, site_id=None):
        data = super(MyCommentForm, self).get_comment_create_data()
        data.update({'qq_num': self.cleaned_data['qq_num']})
        return data


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'message', 'email', 'subject']
