from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import *

app_name = "Perfil"

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)