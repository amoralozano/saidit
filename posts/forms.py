from django import forms
from saidituser.models import SaidItUser
from django.utils import timezone

class AddPostForm(forms.Form):
    user = forms.ModelChoiceField(queryset=SaidItUser.objects.all())
    body = forms.CharField(max_length=150)
    # time_created = forms.DateTimeField()