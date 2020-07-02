from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('aboutus', views.about, name="aboutus"),
    path('news', views.news, name="news"),
    path('contact', views.contact, name="contact"),
    path('destinations', views.destinations, name="destinations"),
    path('elements', views.elements, name="elements"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)