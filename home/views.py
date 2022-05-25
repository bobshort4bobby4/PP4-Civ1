
from django.views.generic import  TemplateView
from roombook.models import RoomType
from reviews.models import Reviews


# Create your views here.


class HomeView(TemplateView): # happpy
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_types'] = RoomType.objects.all()
        # only showcase reviews which are featured
        context['reviews'] = Reviews.objects.filter(featured= True)
        return context

class InfoView(TemplateView):# happy
    template_name = 'home/info.html'


class StaffView(TemplateView):# happy
    template_name = 'home/staff.html'


