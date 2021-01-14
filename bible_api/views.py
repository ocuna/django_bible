from django.shortcuts import render, redirect
from django.db import models
from rest_framework import viewsets
from . models import BRB_Verses
from . serializers import BRB_Verses_Serializer


def home(request):

	context = {
		'test': models.Model.__dict__
	}

	return render(request, 'home.html', context)

class BRB_Verses_View(viewsets.ModelViewSet):
	queryset = BRB_Verses.objects.all() 
	serializer_class = BRB_Verses_Serializer