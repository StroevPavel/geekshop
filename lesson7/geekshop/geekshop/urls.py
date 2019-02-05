from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from django.urls import path
from django.contrib import admin
import mainapp.views as mainapp


urlpatterns = [
    path('', mainapp.main, name='main'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('unit/<int:pk>/', mainapp.unit, name='unit'),
    path('base/', mainapp.base),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('admin/', include('adminapp.urls', namespace='admin'))
    # path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)