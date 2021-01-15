from django.shortcuts import render, redirect
from django.db import models

#imports from the rest_framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

#my data I'm working with
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

# this is a decorator being imported from  rest_framework
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
# The @api_view decorator for working with function based views.
class bcv_lookup(viewsets.ReadOnlyModelViewSet):
    queryset = BRB_Verses.objects.all()
    serializer_class = BRB_Verses_Serializer
    lookup_field = 'book'

    @action(detail=True)
    def book_names(self, request, pk=None):
        book = self.get_object().filter(book=book)
        return Response(book)