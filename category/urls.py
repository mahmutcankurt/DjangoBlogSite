from .views import index_view
from django.urls import path

app_name = "category"

urlpatterns = [
    path('', index_view),
]
