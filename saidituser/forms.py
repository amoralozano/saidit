from django import forms
from django.forms import fields

from saidituser.models import SaidItUser



class UserProfile(forms.ModelForm):
    # display_name = models.CharField(max_length=30)
    # age = forms.IntegerField(null=True, blank=True)
    # bio = forms.CharField(widget=forms.TextInput, null=True, blank=False)
    class Meta:
        model = SaidItUser
        fields = ['display_name', 'age', 'bio', 'image']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = SaidItUser
        fields = ['display_name', 'age', 'bio', 'image']
   