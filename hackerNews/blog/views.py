from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, get_object_or_404
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

from .forms import RegisterUserForm, ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.

def index(request):
    articles = Article.objects.all()
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context={'articles':articles})

@login_required
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
			aux.article = Article.objects.get(pk=pk)
			if request.user.is_authenticated:
				aux.person = request.user
			aux.save()
			return redirect('home')
	else:
		form = CommentForm()
	return render(request, 'comments.html', context={'form':CommentForm, 'comments':comments})

"""class BookListView(generic.ListView):
    model = Article

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):

    Generic class-based view listing books on loan to current user. 
    model = Article
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
"""

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
def new_comment(request, id):
	try:
		artic = Article.objects.get(pk=id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			aux = form.save(commit=False)
			aux.article = artic
			if request.user.is_authenticated():
				aux.person = request.user
			aux.save()
			return redirect('home')
	else:
		form = CommentForm()
	return render(request, 'new_comment.html', {'form': form})