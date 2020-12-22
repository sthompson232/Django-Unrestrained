from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import AddComment, FredQuery, FilmRating, films
from .models import Comment, FredQueryData, FilmRatings
from .utils import get_plot, get_prices, get_fred_query, get_graph, get_variance, get_bar, get_barh
from datetime import datetime



def index(request):
    return render(request, 'django_app/index.html', {'title': 'Home'})


##########################################################################################################################################

@login_required
def finance(request):

    # FRED QUERY FORM
    if request.method == 'POST' and 'query' in request.POST:
        fred_form = FredQuery(request.POST)

        if fred_form.is_valid():
            # CREATING A VARIABLE FOR EACH PIECE OF DATA ENTERED
            start_date = fred_form.cleaned_data['start_date']
            end_date = fred_form.cleaned_data['end_date']
            data_type = fred_form.cleaned_data['data_type']
            author_id = request.user.id

            # SAVING QUERY TO SQL DB
            new_fred_query = FredQueryData(start_date=start_date, end_date=end_date, data_type=data_type, author_id=author_id)
            new_fred_query.save()
            return HttpResponseRedirect('/finance')

    else:
        fred_form = FredQuery()


    # GETS MOST RECENT QUERY FROM DB
    if FredQueryData.objects.filter(author = request.user.id).reverse().first():
        latest_query = FredQueryData.objects.filter(author = request.user.id).reverse().first()
        data_type = latest_query.data_type
        start_date = latest_query.start_date
        end_date = latest_query.end_date

        # GRAPH VARIABLE EQUALS PANDAS DATAFRAME
        graph = get_fred_query(data_type, start_date, end_date)
        variance = get_variance(data_type, start_date, end_date)
    else:
        graph = get_fred_query("SP500", '2015, 1, 1', '2016, 1, 1')
        variance = get_variance("SP500", '2015, 1, 1', '2016, 1, 1')


    # ADD COMMENT FORM
    if request.method =='POST' and 'comment' in request.POST:
        form = AddComment(request.POST)
        print(form.data)
        if form.is_valid():
            content = form.cleaned_data['comment']
            page = "finance"
            author_id = request.user.id
            new_comment = Comment(content=content, page=page, author_id=author_id)
            new_comment.save()
            return HttpResponseRedirect('/finance')

    else:
        form = AddComment()

    # LIST EXISTING COMMENTS
    comments = Comment.objects.filter(page="finance")

    return render(request, 'django_app/finance.html', {"title":"The Stock Market", "form":form, "fred_form":fred_form, "comments":comments, "graph":graph, "variance":variance})



##########################################################################################################################################

@login_required
def data_analysis(request):

    if request.method == 'POST' and 'rating' in request.POST:
        rating_form = FilmRating(request.POST)

        if rating_form.is_valid():
            # VARIABLES EQUAL FORM DATA
            film = rating_form.cleaned_data['film']
            rating = rating_form.cleaned_data['rating']
            author_id = request.user.id
            # VARIABLE EQUALS NEW DB ENTRY
            new_rating = FilmRatings(film=film, rating=rating, author_id=author_id)

            # IF RATING WITH SAME AUTHOR ID AND FILM EXISTS
            if FilmRatings.objects.filter(author = request.user.id, film = film):
                # DELETE THE PAST RATING
                FilmRatings.objects.filter(author = request.user.id, film = film).delete()
                # SAVE DB ENTRY
                new_rating.save()
                return HttpResponseRedirect('/data-analysis')    
            else:
                new_rating.save()
                return HttpResponseRedirect('/data-analysis')

    else:
        rating_form = FilmRating()



    # IF CURRENT USER HAS ANY RATINGS ON DB
    if FilmRatings.objects.filter(author = request.user.id).all():
        # THEN VARIABLE EQUALS ALL EXISTING RATINGS
        my_ratings = FilmRatings.objects.filter(author = request.user.id).all()
        my_films = my_ratings.values('film')
        my_points = my_ratings.values('rating')
        # NEED FILM AND RATINGS VALUES AND THEN APPLY THEM TO X AND Y

        x_rating = []
        y_film = []

        for elem in my_films:
            for film in elem.values():
                y_film.append(film)

        for elem in my_points:
            for point in elem.values():
                x_rating.append(point)


        chart = get_barh(x_rating, y_film)
    else:
        chart = get_bar(films, [(x, x) for x in range(11)])

        # ADD COMMENT FORM
    if request.method =='POST' and 'comment' in request.POST:
        form = AddComment(request.POST)
        if form.is_valid():
            content = form.cleaned_data['comment']
            page = "data_analysis"
            author_id = request.user.id
            new_comment = Comment(content=content, page=page, author_id=author_id)
            new_comment.save()
            return HttpResponseRedirect('/data-analysis')

    else:
        form = AddComment()

    # LIST EXISTING COMMENTS
    comments = Comment.objects.filter(page="data_analysis")
    return render(request, 'django_app/data_analysis.html', {"title":"Data Analysis", "form":form, "comments":comments, "rating_form":rating_form, "chart":chart})



##########################################################################################################################################

@login_required
def test(request):
    return render(request, 'django_app/test.html')