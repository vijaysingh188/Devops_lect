from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from devops_app.models import Devops
from devops_app.forms import DevopsUploadForm


# Create your views here.

class DevopsClassBasedView(TemplateView):
    def get(self,request):
        form = DevopsUploadForm()
        # obj = Devops.objects.values("name","vedio_file","choose_month","Date")
        obj = Devops.objects.all()


        return render(request,'devops.html',{'obj':obj,'form':form})
    
    def post(self,request):
        form = DevopsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('DevopsClassBasedView') 
        return render(request,'devops.html')
