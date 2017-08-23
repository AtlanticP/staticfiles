from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'project/index.html'), name = 'start'),
     # url(r'^$', views.start, name = 'start'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	