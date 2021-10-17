from django import forms
from saidituser.models import SaidItUser
from django.utils import timezone
from group.models import SubGroup

class AddPostForm(forms.Form):
    body = forms.CharField(max_length=150)

