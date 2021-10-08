from django import forms
from saidituser.models import SaidItUser
from django.utils import timezone
from group.models import SubGroup

class AddPostForm(forms.Form):
    user = forms.ModelChoiceField(queryset=SaidItUser.objects.all())
    body = forms.CharField(max_length=150)
    posted_in = forms.ModelChoiceField(queryset=SubGroup.objects.all())

