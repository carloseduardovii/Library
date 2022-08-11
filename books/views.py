from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, BookItem, User
from .serializers import BookSerializer, BookItemSerializer, BookItemCreateSerializer
from .permisions import IsLibraryUser, IsRent
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [IsLibraryUser]

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return BookItemCreateSerializer
        else:
            return  BookItemSerializer

    def get_permissions(self):
        if self.action ==  "update":
            permissions = [ IsRent]
            return [permission() for permission in permissions]
        else:
            return [IsLibraryUser()]
