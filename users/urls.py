from django.conf.urls import url
from .views import signup

urlpatterns = [
    url(r'^register/$', signup, name='register'),

]

