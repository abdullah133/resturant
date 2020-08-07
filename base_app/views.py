from django.shortcuts import render
from django.views.generic.base import TemplateView






class HomeView(TemplateView):
    template_name = 'base_app/home.html'


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
