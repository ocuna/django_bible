from re import search
from django.shortcuts import render, redirect

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

def brb(request, book, chapter, range):
    re_result = None
    book_code = book
    bookDisplay = None
    verse_1 = None
    verse_2 = None
    total_verses = None
    bcvCode_1 = None
    bcvCode_2 = None
    verses = {}
    verseHTML = ''


    # regex: ^([0-9]{1,3})-([0-9]{1,3})$
    # group1 = verse 1, group2 = verse 2 
    if  search(r'^([0-9]{1,3})-([0-9]{1,3})$', range):
        re_result = search(r'^([0-9]{1,3})-([0-9]{1,3})$', range)
        verse_1 = int(re_result.group(1))
        verse_2 = int(re_result.group(2))
        total_verses = verse_2 - verse_1
        bcvCode_1 = str(book).lower() + str(chapter) + ":" + str(verse_1)
        bcvCode_2 = str(book).lower() + str(chapter) + ":" + str(verse_2)

        v1 = BRB_Verses.objects.filter(bcvCode=bcvCode_1).all()
        v2 = BRB_Verses.objects.filter(bcvCode=bcvCode_2).all()

        if v1 and v2:
            verses = BRB_Verses.objects.filter(book=book,chapterNumber=chapter,verseNumber__range=(verse_1, verse_2)).values('bookDisplay','verse', 'verseNumber')
            bookDisplay = verses.values('bookDisplay')[0]['bookDisplay']
            count = 0
            for row in verses:
                verseHTML += "<li>" + str(verses[count]['verseNumber']) + ":  " + verses[count]['verse'] + "</li>"
                count += 1


    elif  search(r'^[0-9]{1,3}$', range):
        re_result = search(r'^[0-9]{1,3}$', range)
        verse_1 = int(re_result.group(0))
        bcvCode_1 = str(book).lower() + str(chapter) + ":" + str(verse_1)

        v1 = BRB_Verses.objects.filter(bcvCode=bcvCode_1).all()

        if v1:
            verses = BRB_Verses.objects.filter(bcvCode=bcvCode_1).values('bookDisplay','verse', 'verseNumber')
            bookDisplay = verses.values('bookDisplay')[0]['bookDisplay']
            verseHTML = "<li>" + str(verses[0]['verseNumber']) + " " + verses[0]['verse'] + "</li>"

#    v1 = BRB_Verses.objects.filter(bcvCode='genesis',chapterNumber=chapter,verseNumber=verse_1).all()
#    q2 = q1.filter(chapterNumber=int(chapter))
#    item = q2.get()

    context = {
        'bookDisplay': bookDisplay,
        'chapter': chapter,
        'verse_1': verse_1,
        'verse_2': verse_2,
        'range': str(range),
        'verseHtml': verseHTML
#        'test': models.Model.__dict__
    }

    return render(request, 'brb.html', context)

def brb_range(request, book, chapter, verseA, verseB):

    context = {
        'book': book,
        'chapter': chapter,
        'range': str(verseA) + "-" + str(verseB),
        'test': models.Model.__dict__
    }

    return render(request, 'brb.html', context)

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