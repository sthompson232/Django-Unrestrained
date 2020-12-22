from django import forms
from .models import FredQueryData

data_types = [
    ("SP500", "S&P 500"), 
    ("NASDAQ100", "NASDAQ-100"), 
    ("DEXUSUK", "U.S. / U.K. Foreign Exchange Rate"), 
    ("CLVMNACSCAB1GQUK", "Real Gross Domestic Product for United Kingdom"), 
    ("GBRCPIALLMINMEI", "Consumer Price Index of All Items in the United Kingdom"),
    ("DEXCHUS", "China / U.S. Foreign Exchange Rate"),
    ("WILL5000IND", "Wilshire 5000 Total Market Index"),
    ("VIXCLS", "CBOE Volatility Index: VIX"),
    ("TOTRESNS", "Total Reserves of Depository Institutions"),
    ("TERMCBCCALLNS", "Commercial Bank Interest Rate on Credit Card Plans, All Accounts"),
    ("INDPRO", "Industrial Production: Total Index"),
    ("PALLFNFINDEXQ", "Global Price Index of All Commodities")
    ]


class DateInput(forms.DateInput):
    input_type = 'date'


class AddComment(forms.Form):
    comment = forms.CharField(label="Add Comment", max_length=200)


class FredQuery(forms.Form):
    data_type = forms.CharField(label="Data Type", widget=forms.Select(choices=data_types))
    start_date = forms.DateField(label="Start Date", widget=DateInput(format='%Y, %m, %d'))
    end_date = forms.DateField(label="End Date", widget=DateInput(format='%Y, %m, %d'))








    # class Meta:
    #     model = FredQueryData
    #     fields = ['start_date', 'end_date', 'data_type']
    #     widgets = {'start_date':DateInput(), 'end_date':DateInput()}

    # start_date = forms.DateField(widget=forms.DateInput(format='%Y, %m, %d'), input_formats=('%Y, %m, %d', ))
    # end_date = forms.DateField(widget=forms.DateInput(format='%Y, %m, %d'), input_formats=('%Y, %m, %d', ))