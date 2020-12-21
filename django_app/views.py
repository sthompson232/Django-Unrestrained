from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import AddComment, FredQuery
from .models import Comment, FredQueryData
from .utils import get_plot, get_prices, get_fred_query, get_graph
from datetime import datetime


def index(request):
    return render(request, 'django_app/index.html', {'title': 'Home'})



##########################################################################################################################################

@login_required
def finance(request):

    # GETS MOST RECENT QUERY FROM DB
    latest_query = FredQueryData.objects.filter(author = request.user.id).first()
    data_type = latest_query.data_type
    start_date = str(latest_query.start_date)
    end_date = str(latest_query.end_date)
    print(start_date)
    print(type(start_date))
    # GRAPH VARIABLE EQUALS PANDAS DATAFRAME
    graph = get_fred_query(data_type, start_date, end_date)
    





    # FRED QUERY FORM
    if request.method == 'POST':
        fred_form = FredQuery(request.POST)

        if fred_form.is_valid():
            # CREATING A VARIABLE FOR EACH PIECE OF DATA ENTERED
            # start_date = datetime(fred_form.cleaned_data['start_date'])
            # end_date = datetime(fred_form.cleaned_data['end_date'])
            start_date = datetime(2011, 1, 1)
            end_date = datetime(2019, 1, 1)
            data_type = fred_form.cleaned_data['data_type']
            author_id = request.user.id

            # SAVING QUERY TO SQL DB
            new_fred_query = FredQueryData(start_date=start_date, end_date=end_date, data_type=data_type, author_id=author_id)
            new_fred_query.save()

    else:
        fred_form = FredQuery()


    # ADD COMMENT FORM
    if request.method =='POST':
        form = AddComment(request.POST)

        if form.is_valid():
            content = form.cleaned_data['comment']
            page = "finance"
            author_id = request.user.id
            new_comment = Comment(content=content, page=page, author_id=author_id)
            new_comment.save()

    else:
        form = AddComment()

    # LIST EXISTING COMMENTS
    comments = Comment.objects.filter(page="finance")

    return render(request, 'django_app/finance.html', {"form":form, "fred_form":fred_form, "comments":comments, "graph":graph})



##########################################################################################################################################

@login_required
def data_analysis(request):


    fred_dataframe = get_prices('NASDAQ100', '2010, 1, 1', '2019, 1, 1')
    # CREATE VARIABLES FOR GRAPH
    x = fred_dataframe.index
    y = fred_dataframe['NASDAQ100']
    title = "Quantity of (US)"
    x_label = "Time"
    y_label = "quantity"
    graph = get_plot(x, y, title, x_label, y_label)



        # ADD COMMENT FORM
    if request.method =='POST':
        form = AddComment(request.POST)

        if form.is_valid():
            content = form.cleaned_data['comment']
            page = "data_analysis"
            author_id = request.user.id
            new_comment = Comment(content=content, page=page, author_id=author_id)
            new_comment.save()

    else:
        form = AddComment()

    # LIST EXISTING COMMENTS
    comments = Comment.objects.filter(page="data_analysis")
    return render(request, 'django_app/data_analysis.html', {"form":form, "comments":comments, "graph":graph})



##########################################################################################################################################

@login_required
def test(request):

    # if form is submitted then do this code with form data
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2020, 1, 1)
    data_type = "SP500"

    # GETS PANDAS DATAFRAME
    fred_dataframe = get_prices(data_type, start_date, end_date)
    fred_dataframe.columns = ['date']
    # CREATE VARIABLES FOR GRAPH
    x = fred_dataframe.index
    y = fred_dataframe["date"].tolist()
    print(y)
    title = f"Quantity of {data_type} (US)"
    x_label = "Time"
    y_label = f"{data_type} quantity"
    chart = get_plot(x, y, title, x_label, y_label)

    return render(request, 'django_app/test.html', {"chart":chart})