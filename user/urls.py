from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.index),
     path('home/', views.index),
     path('', views.index),
     path('aboutus/', views.aboutus),
     path('contact/', views.contact),
     path('gallery/', views.gallery),
     path('video/', views.video),
     path('news/', views.news),
     path('login/', views.login),
     path('viewnews/', views.viewnews),
     path('details/', views.ndetails),
     path('trendnews/', views.trendnews),
     path('slidenews/', views.slidenews),
     path('citynews/', views.citynews),
     path('videodetails/', views.videodetails),
     path('insta',views.insta, name="insta"),
     path('facebook',views.facebook, name="facebook"),
     path('youtube',views.youtube, name="youtube"),
     path('linkdin',views.linkdin, name="linkdin"),
]