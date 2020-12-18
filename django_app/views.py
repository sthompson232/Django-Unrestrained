from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import AddComment
from .models import Comment


def index(request):
    return render(request, 'django_app/index.html', {'title': 'Home'})



@login_required
def finance(request):

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

    return render(request, 'django_app/finance.html', {"form":form, "comments":comments})



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