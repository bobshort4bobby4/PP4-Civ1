
from django.views.generic import  TemplateView


# Create your views here.
class HomeView(TemplateView): # happpy
    template_name = "home/home.html"
