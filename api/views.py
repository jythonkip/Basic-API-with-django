from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Persons
from rest_framework import permissions, authentication
from .permissions import UserPerm
from .serializers import PersonsSerializers


# Create your views here.
class ListPersonsAPIView(ListAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm]
    authentication_classes = [authentication.SessionAuthentication]


# class RetrievePersonsAPIView(RetrieveAPIView):
#     queryset = Persons.objects.all()
#     serializer_class = PersonsSerializers
#     lookup_field = 'id'
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm]
#     authentication_classes = [authentication.SessionAuthentication]


class RetrieveUpdateDestroyPersonsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm]
    authentication_classes = [authentication.SessionAuthentication]
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
class CreatePersonsAPIView(CreateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm]
    authentication_classes = [authentication.SessionAuthentication]

# class DestroyPersonsAPIView(DestroyAPIView):
#     queryset = Persons.objects.all()
#     serializer_class = PersonsSerializers
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm]
#     authentication_classes = [authentication.SessionAuthentication]