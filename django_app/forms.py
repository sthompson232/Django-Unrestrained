from django import forms
from .models import FredQueryData

class AddComment(forms.Form):
    comment = forms.CharField(label="Add Comment", max_length=200)


class FredQuery(forms.ModelForm):
    start_date = forms.CharField(label="Start Date (yyyy, mm, dd)")
    end_date = forms.CharField(label="End Date (yyyy, mm, dd)")
    data_type = forms.CharField(label="Data Type", max_length=50)

    class Meta:
        model = FredQueryData
        fields = ['start_date', 'end_date', 'data_type']

    start_date = forms.DateField(widget=forms.DateInput(format='%Y, %m, %d'), input_formats=('%Y, %m, %d', ))
    end_date = forms.DateField(widget=forms.DateInput(format='%Y, %m, %d'), input_formats=('%Y, %m, %d', ))