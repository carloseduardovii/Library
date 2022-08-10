from dataclasses import fields
from rest_framework import serializers
from .models import Book, BookItem, User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields = ("title", "author")
        
class MemberSerializer:
    class Meta:
        fields = "email", "first_name"

class BookItemSerializer(serializers.ModelSerializer):
    book = BookReadSerializer()
    member = MemberSerializer()
    class Meta:
        model =BookItem
        fields = "__all__"
        
class BookItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BookItem