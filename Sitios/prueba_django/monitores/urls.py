from django.urls import path
from .views import monitor

urlpatterns = [
    path('monitores/',monitor, name='monitores'),
]