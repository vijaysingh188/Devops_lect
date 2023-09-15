from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from devops_app.models import Devops
from devops_app.forms import DevopsUploadForm


# Create your views here.

class DevopsClassBasedView(TemplateView):
    def get(self,request):
        
        # obj = Devops.objects.values("name","vedio_file","choose_month","Date")
        obj = Devops.objects.all()[:3]

        return render(request,'devops.html',{'obj':obj})
    
    def post(self,request):
        Courses = request.POST.get("Courses")
        Month = request.POST.get("Month")
        date = request.POST.get("date")
        print(Courses,'======================',Month,'=========',date)
        mydict = {}
        
        if date:
            mydict['new_obj'] = Devops.objects.filter(name = Courses,choose_month=Month,Date=date).all()
        else:
            mydict['new_obj'] = Devops.objects.filter(name = Courses,choose_month=Month).all()
            
        return render(request,'devops.html',{'mydict':mydict})
    
    
    
class DevopsUploadFile(TemplateView):
    def get(self,request):
        form = DevopsUploadForm()

        return render(request,'devops_upload.html',{'form':form})
    
    def post(self,request):
        form = DevopsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('DevopsClassBasedView') 
        return render(request,'devops.html')
