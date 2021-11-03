from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from .forms import form1

# Create your views here.

@login_required(login_url="login")
def home(request):
	cacaform = form1(request.POST)
	if request.method == "POST":
		if cacaform.is_valid():
			print(cacaform.cleaned_data['UserType'])
			
	context = {}
	context['form'] = form1
	return render(request, "index.html", context=context)