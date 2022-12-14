from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('propiedades/', include('propiedades.urls')),
    path('terrenos/', include('terrenos.urls')),
    path('ventas/', views.ventas, name='ventas'),
    path('alquileres/', views.alquileres, name='alquileres')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)