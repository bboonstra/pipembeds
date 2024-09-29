"""
URL configuration for pipembeds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index page
    path('json/<str:name>/', views.get_json, name='get_json'),  # URL for JSON response
    path('html/<str:name>/', views.get_html, name='get_html'),  # URL for HTML card
    re_path(r'^.*$', views.index),  # Wildcard pattern to catch any other path
]

