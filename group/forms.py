from django import forms
from saidituser.models import SaidItUser
# previusly had AddSubGroup


class AddSubGroup(forms.Form):
    group_name = forms.CharField(max_length=50)
    group_description = forms.TextInput()
    # time_created =
