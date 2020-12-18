from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AddComment
from .models import Comment


def index(request):
    return render(request, 'django_app/index.html', {'title': 'Home'})



def about(request):
    return render(request, 'django_app/about.html', {'title': 'About'})



def form_page(request):

    if response.method == "POST":
        form = AddComment(request.POST)
    else:
        form = AddComment()
    
    if form.is_valid():
        comment = form.cleaned_data["comment"]
        t = Comments(comment=comment)


    return render(request, 'django_app/test.html', {'form':form})


@login_required
def finance(request):
    comments = {
        'comments': Comment.objects.filter(page="finance")
    }
    return render(request, 'django_app/finance.html', comments)


@login_required
def data_analysis(request):
    comments = {
        'comments': Comment.objects.filter(page="data_analysis")
    }
    return render(request, 'django_app/data_analysis.html', comments)