from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "Main"

urlpatterns = [
    path('', views.index, name='index'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)