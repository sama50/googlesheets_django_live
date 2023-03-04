from django.contrib import admin
from django.urls import path 
from app.views import home , index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'index'),
    path('room/<str:id>/',home, name= 'room'),
]
