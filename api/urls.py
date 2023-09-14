from django.urls import path
from .views import (
    ListPersonsAPIView,
    RetrieveUpdateDestroyPersonsAPIView,
    CreatePersonsAPIView
)

urlpatterns = [
    path('list/', ListPersonsAPIView.as_view(), name='list'),
    path('<int:id>/',  RetrieveUpdateDestroyPersonsAPIView.as_view(), name='retrieve_update_delete'),
    path("", CreatePersonsAPIView.as_view(), name='create')
]