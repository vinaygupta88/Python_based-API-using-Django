from django.contrib import admin
from django.urls import path
from API.views import AppList,Appinfo,home

urlpatterns = [
     path('', home, name='home'),
    path('api/AppDetails',AppList.as_view()),
    path('api/AppDetails/<int:pk>',Appinfo.as_view()),
    path('admin/', admin.site.urls),
]
