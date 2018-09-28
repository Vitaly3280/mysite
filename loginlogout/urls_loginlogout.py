
from django.urls import re_path
from . import log_views

urlpatterns = [
    re_path(r'in/', log_views.login),
    re_path(r'^out/', log_views.logout),
]
