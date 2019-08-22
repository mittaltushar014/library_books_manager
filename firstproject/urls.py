"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from testapp import views as testapp_views
from django.conf.urls import url,include
from exam import views as exam_views
#import django.urls import include,path,url

urlpatterns = [
    url('testapp',include('testapp.urls')),
    url('exam',include('exam.urls')),
    url('BRMapp',include('BRMapp.urls')),
    # path('about/',testapp_views.about),
    #path('showTest/',exam_views.showTest),
    #path('showResult/',exam_views.showResult),

    #path('showContact/',testapp_views.showContact),
    #url('^$',testapp_views.greeting),*/
    path('admin/', admin.site.urls),
]
