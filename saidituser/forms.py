from django import forms



class UserProfile(forms.Form):
    # display_name = models.CharField(max_length=30)
    age = forms.IntegerField(null=True, blank=True)
    bio = forms.CharField(widget=forms.TextInput, null=True, blank=False)
   