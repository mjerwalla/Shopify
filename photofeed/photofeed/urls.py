"""photofeed URL Configuration

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
from feed.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('push_feed', push_feed), 
    path('share_pic/<slug:pic_id>', share_pic),
    path('get_share', get_share_url),
    path('delete_all', delete_all),
    path('delete_one', delete_one),
    path('pusher_authentication', pusher_authentication)
]
