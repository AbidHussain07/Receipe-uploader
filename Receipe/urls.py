"""
URL configuration for Receipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from Home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home , name="Homepage"),
    path('login/',login_page , name="Login"),
    path('logout/',logout_page , name="Logout"),
    path('register/',registration , name="Registration"),
    path('receipes/',receipes , name="Receipes"),
    path('details-receipes/<id>',see_receipe , name="Detail-Receipes"),
    path('about/',about_us , name="About-us"),
    # path('feedback/',feedback , name="FeedBack"),
    path('add-receipe/',add_receipe , name="Adding-Receipe"),
    path('update-receipe/<id>/',update_receipe , name="Update-Receipe"),
    path('delete-receipe/<id>/',delete_receipe , name="Deleted-Receipe"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()