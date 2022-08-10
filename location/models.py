from tkinter import Pack
from django.db import models

from books.models import BookItem
# Create your models here.
class Place(models.Model):
    floor = models.IntegerField()
    name_room = models.CharField(max_length=100)

    def __str__(self):
        return f"Floor: {self.floor} - Name Room: {self.name_room}"

class BookItemPlace(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Place: {self.place} - Book: {self.book_item}"