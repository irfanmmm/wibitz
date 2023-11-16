from django.contrib import admin
from django.urls import path, include
from web.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls",namespace="web")),

    # path('', index),

    # image add ceyyunnundengil must ayittum add akkanm
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
