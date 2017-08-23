import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/project/'

STATICFILES_DIR = os.path.join(BASE_DIR, 'static')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/music/'

PROJECT_DIR=os.path.dirname(__file__)

# urlpatterns = [
#     # url(r'^$', TemplateView.as_view(template_name = 'project/index.html'), name = 'start'),
#      url(r'^$', views.start, name = 'start'),
# ]
# if settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def start(request):
	return HttpResponse(urlpatterns)


# Create your views here.
