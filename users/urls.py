from django.conf.urls import url
from .views import signupView, activate, account_activation_sent, user_login, user_logout, user_edit_profile, user_change_password

urlpatterns = [
    url(r'^register/$', signupView, name='register'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate,
        name='activate'),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='user_logout'),
    url(r'^user_edit_profile/$', user_edit_profile, name='user_edit_profile'),
    url(r'^change_password/$', user_change_password, name='change_password'),


]

