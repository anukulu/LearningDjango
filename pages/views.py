from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
# 	return render(request, 'pages/homepage.html')

class HomePageView(TemplateView):
	template_name = "pages/homepage.html"

class AboutPageView(TemplateView):
	template_name = "pages/about.html"

		