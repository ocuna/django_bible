from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . apirouters import BCV_Lookup

router = routers.DefaultRouter()
# router.register('brb_verses', views.BRB_Verses_View)
# router.register('^verses/{limit}/$', views.verses_list_limit,'brb_verses')
# router.register('^verses_detail/{pk}/$', views.verses_list_limit,'brb_verses')

#from apirouters.py 
#book_router = BCV_Lookup()
#book_router.register('book', views.bcv_lookup, 'book')

urlpatterns = [
    path('', views.home, name='home'),
    path('book/{prefix}', views.bcv_lookup, name='book'),
]

# urlpatterns = format_suffix_patterns(router.urls) + format_suffix_patterns(book_router.urls)

