from django.shortcuts import render, redirect
from django.db import models

def home(request):

	context = {
		'test': models.Model.__dict__
	}

	return render(request, 'home.html', context)