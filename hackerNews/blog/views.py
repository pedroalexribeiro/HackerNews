from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import permission_required

from .forms import RegisterUserForm, ArticleForm, CommentForm
from .models import Article, Comment, Vote

# Create your views here.

def index(request):
    article_list = Article.objects.all()
    for article in article_list:
    	try:
    		vote = article.votes.get(person__username = request.user.username, article__id = article.id)
    	except Vote.DoesNotExist:
    		article.upvote = False
    		article.save()
    		if vote.has_voted == True:
    			article.upvote = True
    		else:
    			article.upvote = False
    page = request.GET.get('page', 1)
    paginator = Paginator(article_list, 30) # Show 25 contacts per page
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(page)
    except EmptyPage:
        articles = paginator.page(paginator.num_page)
    return render(request, 'index.html', context={'articles':articles})

def article(request, pk):
	try:
		article = Article.objects.get(pk=pk)
		comments = Comment.objects.filter(article = article)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			aux = form.save(commit=False)
			aux.article = article
			if request.user.is_authenticated:
				aux.person = request.user
			aux.save()
			return redirect('home')
	else:
		form = CommentForm()
		return render(request, 'view_article.html', context={'article':article, 'form':CommentForm, 'comments':comments})

def register_user(request):
	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
		    form.save()
		    username = form.cleaned_data.get('username')
		    raw_password = form.cleaned_data.get('password1')
		    user = authenticate(username=username, password=raw_password)
		    login(request, user)
		    return redirect('home')
	else:
		form = RegisterUserForm()
	return render(request, 'registration/register_new_user.html', {'form': form})

def comments(request, pk):
	try:
		article = Article.objects.get(pk=pk)
		comments = Comment.objects.filter(article = article)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			aux = form.save(commit=False)
			aux.article = article
			if request.user.is_authenticated:
				aux.person = request.user
			aux.save()
			return redirect('home')
	else:
		form = CommentForm()
	return render(request, 'comments.html', context={'form':CommentForm, 'comments':comments})

@login_required
def new_article(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ArticleForm()
	return render(request, 'new_article.html', {'form': form})

@login_required
def vote(request, pk):
	try:
		article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	try:
		vote = article.votes.get(person__username = request.user.username, article__id = article.id)
	except Vote.DoesNotExist:
		aux = Vote.objects.create()
		if request.user.is_authenticated:
			aux.person = request.user
		aux.has_voted  = True
		aux.article = article
		aux.save()
		article.save()
		return redirect('home')
	if vote.has_voted:
		vote.has_voted = False
		article.upvote = False
	else:
		vote.has_voted = True
		article.upvote = True
	article.save()
	vote.save()
	return redirect('home')

@login_required
@permission_required('catalog.can_change_status')
def hide(request, pk):
	try:
		article = Article.objects.get(pk=pk)
		article.visible = False
		article.save()
		return redirect('home')
	except Article.DoesNotExist:
		raise Http404("Article does not exist")