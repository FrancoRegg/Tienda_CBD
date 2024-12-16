from django.contrib import admin
from django.urls import path, re_path ,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.productos.urls')),
    path('', include('apps.pedidos.urls')),
    path('', include('apps.usuarios.urls')),
    path('', include('apps.envios.urls')),
    path('', include('apps.pagos.urls'))
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),
]