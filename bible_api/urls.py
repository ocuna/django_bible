from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('brb_verses', views.BRB_Verses_View)


urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls))
]
