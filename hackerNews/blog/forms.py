from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment

class RegisterUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text="Enter your First Name.")
	last_name = forms.CharField(max_length=30, required=True, help_text="Enter your Last Name.")
	email = forms.EmailField(max_length=254, help_text="Enter your e-mail")

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'link',]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
