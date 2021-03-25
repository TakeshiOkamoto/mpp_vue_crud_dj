from django.urls import path
from .views import IndexView
from .views import InitView
from .views import APIView

app_name = 'vue_crud_data'

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('init/', InitView.as_view(), name='init'),
   path('api/', APIView.as_view(), name='api'),
]