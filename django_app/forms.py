from django import forms

class AddComment(forms.Form):
    comment = forms.CharField(label="Add Comment", max_length=200)


class FredQuery(forms.Form):
    # start_date = forms.
    # end_date = 
    data_type = forms.CharField(label="Data Type", max_length=50)