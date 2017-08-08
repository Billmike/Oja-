from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, FarmerProfile, SendQuotes
from .forms import PostForm, SendQuotesForm, SignUpForm, FarmerSignUpForm
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.views.generic import View


User = get_user_model()
def post_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Product created successfully.")
		return HttpResponseRedirect("/posts/dashboard/")
	context = {
	"form":form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
	"title":instance.product_name,
	'user': request.user,
	"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_update(request, id):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Update successfull.")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"title": instance.product_name,
	"instance": instance,
	"form":form,
	}
	return render(request, "post_form.html", context)

def view_profile(request):
	farmer_title = "Farmer Profile"
	first_name = FarmerProfile.objects.filter(first_name="first_name", last_name="last_name")
	instance = first_name
	context = {
	    "title": farmer_title,
        "instance": instance,

	}
	return render(request, "profile.html", context)

def post_delete(request):
	return HttpResponse("<h1>Delete Shows!</h1>")

def post_list(request):
	query = request.GET.get("f")
	queryset_list = Post.objects.all()
	if query:
		queryset_list = queryset_list.filter(product_name__icontains=query)
	paginator = Paginator(queryset_list, 10)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, produce the first page
		queryset = paginator.page(1)
	except EmptyPage:
		#if Page is out of range, deliver the last page
		queryset = paginator.page(paginator.num_pages)
	"""if request.user.is_authenticated():
			return render(request, "farmer_dashboard.html")"""
	context = {
	"object_list":queryset,
	"title":"Market Place",
	"page_request_var": page_request_var
	}

	return render(request, "post_list.html", context)

def send_quotes(request):
	form = SendQuotesForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		instance.save()
		messages.success(request, "Quotes sent successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form": form,
	}
	return render(request, "send_quotes.html", context)

def farmer_dashboard(request):
	queryset = SendQuotes.objects.filter(id=1)
	context = {
	"object_list": queryset,
	'user': request.user,
	}
	return render(request, "trialdb.html", context)

def sign_up(request):
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		messages.success(request, "Registration Successful")
		return HttpResponseRedirect("/posts/login")
	context = {
	"form":form,
	}

	return render(request, "farmer_sign_up.html", context)

#Main signup view
def farmer_sign(request):
	if request.method == 'POST':
		form = FarmerSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect("/posts/tempdb/")
	else:
		form = FarmerSignUpForm()
	return render(request, "farmer_sign_up.html", {'form':form})

#View for the Charts
class ChartData(APIView):
	"""docstring for ListUsers"""
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		data = {
		"sales": 100,
		"customers":10,
		"users": User.objects.all().count()
		}
		return Response(data)

#View for the chart
class ChartView(View):
	"""docstring for ChartView"""
	def get(self, request, *args, **kwargs):
		return render(request, "charts.html")

#Temporary Dashboard View
def temp_view(request):
	queryset = SendQuotes.objects.filter(id=1)
	context = {
	"object_list": queryset,
	'user': request.user,
	}
	return render(request, "trialdb.html", context)
		
