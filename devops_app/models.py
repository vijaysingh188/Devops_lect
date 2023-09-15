from django.db import models

month = [
    ("Jan","Jan"),
    ("Feb","Feb"),
    ("Mar","Mar"),
    ("Apr","Apr"),
    ("May","May"),
    ("Jun","Jun"),
    ("Jul","Jul"),
    ("Aug","Aug"),
    ("Sep","Sep"),
    ("Oct","Oct"),
    ("Nov","Nov"),
    ("Dec","Dec")
]

branch = [
    ("Devops","Devops"),
    ("AWS","AWS"),
    ("Others","Others")
]


# Create your models here.
def get_media_url(instance,filename):
    return 'media/lectures/dev/{}/{}'.format(instance.choose_month,filename)

class Devops(models.Model):
    name  = models.CharField(max_length=6,choices=branch)
    vedio_file = models.FileField(upload_to=get_media_url,null=True,blank=True)
    choose_month = models.CharField(max_length=3,choices=month)
    Date = models.DateField(null=True, blank=True)
    created_on = models.DateField(auto_now=True, blank=False, null=False)
    updated_on = models.DateField(auto_now_add=True, blank=False, null=False)
    comments  = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return "{}/{}".format(self.name,self.choose_month)
    

