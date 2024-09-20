"""regform_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from attendancesystem import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('formpage', views.formpage, name="formpage"),
    path('read_java', views.read_java, name="read_java"),
    path('read_python', views.read_python, name="read_python"),
    path('read_tally', views.read_tally, name="read_tally"),
    path('read_typewriting', views.read_typewriting, name="read_typewriting"),
    path('read_noleave', views.read_noleave, name="read_noleave"),
    path('read_oneweekleave', views.read_oneweekleave, name="read_oneweekleave"),
    path('allcoursestudents',views.allcoursestudents,name="allcoursestudents"),
    path('biometricuploadfile', views.biometricuploadfile, name="biometricuploadfile"),
]

