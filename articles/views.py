from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def article_list(request):
    article = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'my_articles':article})

def article_detail(request,slug):
    # return HttpResponse(slug)
    arts = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article_detailings':arts})


@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method=='POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article_lists:lists')

    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'forms_are':form})

# accounts: this name previously named as accounts_app so that I was getting 
# error In root url file whatever you'll pass with same name create
# app_name as accounts.