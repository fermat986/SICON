__author__ = 'Fernando'
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^repuesto/crear',listar_repuesto),
)