from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, BookItem, User
from .serializers import BookSerializer, BookItemSerializer, MemberSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer