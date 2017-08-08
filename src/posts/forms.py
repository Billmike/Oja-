from django import forms

from .models import Post, SendQuotes, FarmerProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		"""docstring for Meta"""
		model = Post
		fields = {
		"product_name",
		"product_description",
		"product_price",
		"product_image",
			
				}

class SendQuotesForm(forms.ModelForm):
	"""docstring for SendQuotes"""
	class Meta:
		"""docstring for Meta"""
		model = SendQuotes
		fields = {
		"name_of_product",
		"qty_of_product",
		"delivery_address",
		"phone_number",
			
				}

class SignUpForm(forms.ModelForm):
	"""docstring for SignUpForm"""
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		"""docstring for Meta"""
		model = FarmerProfile
		fields = {
		"first_name",
		"last_name",
		"user_name",
		"email_address",
		"farm_produce",
		"business_address",
		"phone_number",

			
				}

class FarmerSignUpForm(UserCreationForm):
	"""Class to create farmer profile"""
	first_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
	product_farmed = forms.CharField(max_length=254, help_text='Enter Farm produce', required=True)

	class Meta:
		"""docstring for Meta"""
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'product_farmed', 'password1', 'password2',)
		

