from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.HomePageView.as_view(), name='homepage'),
	path('about/', views.AboutPageView.as_view(), name='about'),
]