from django import forms

class AddComment(forms.Form):
    comment = forms.CharField(label="Add Comment", max_length=200)
