# myobject/web/urls.py

from django.urls import path

from web.views import index

urlpatterns = [
   path('', index.index, name="index"),
]