from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.

class DevopsClassBasedView(TemplateView):
    def get(self,request):
        return render(request,'devops.html')
