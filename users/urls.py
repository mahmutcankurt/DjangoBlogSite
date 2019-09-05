from django.conf.urls import url
from .views import signup, activate, account_activation_sent

urlpatterns = [
    url(r'^register/$', signup, name='register'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

]

