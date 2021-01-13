from django.shortcuts import render, redirect

def home(request):

	context = {
		'test': 'test'
	}

	return render(request, 'home.html', context)