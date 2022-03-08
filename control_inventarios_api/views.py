from django.shortcuts import render

# Create your views here.
# control_inventarios/views.py
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "inventarios.html"


class AboutPageView(TemplateView):  # new
    template_name = "about.html"