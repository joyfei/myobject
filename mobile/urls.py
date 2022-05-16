# myobject/mobile/urls.py

from django.urls import path

from web.views import index

urlpatterns = [
   path('', index.index, name="mobile_index"),
]