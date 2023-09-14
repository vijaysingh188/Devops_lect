from django.conf.urls import url
from .scripts.devopsfile import DevopsClassBasedView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^dev_lect',DevopsClassBasedView.as_view(),name="dev_lect")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
