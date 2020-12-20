from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import AddComment, FredQuery
from .models import Comment
from .utils import get_plot, get_prices
from datetime import datetime


def index(request):
    return render(request, 'django_app/index.html', {'title': 'Home'})



@login_required
def finance(request):


    # if form is submitted then do this code with form data
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2020, 1, 1)
    data_type = "SP500"

    # GETS PANDAS DATAFRAME
    fred_dataframe = get_prices(data_type, start_date, end_date)

    # CREATE VARIABLES FOR GRAPH
    x = fred_dataframe.index
    y = fred_dataframe[data_type]
    title = f"Quantity of {data_type} (US)"
    x_label = "Time"
    y_label = f"{data_type} quantity"
    chart = get_plot(x, y, title, x_label, y_label)


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

    return render(request, 'django_app/finance.html', {"form":form, "comments":comments, "chart":chart})



@login_required
def data_analysis(request):
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
    return render(request, 'django_app/data_analysis.html', {"form":form, "comments":comments})