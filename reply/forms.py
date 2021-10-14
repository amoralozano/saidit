from django import forms


class ReplyForm(forms.Form):
    reply_text = forms.CharField(widget=forms.Textarea)