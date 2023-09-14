from django.conf.urls import url
from .scripts.devopsfile import DevopsClassBasedView

urlpatterns = [
    url(r'^dev_lect',DevopsClassBasedView.as_view(),name="dev_lect")

]
