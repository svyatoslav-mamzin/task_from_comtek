from django.db import models


# Create your models here.

class ReferenceBook(models.Model):
    # справочник
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    description = models.TextField()
    version = models.CharField(max_length=10, unique=True)
    initial_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.short_name)


class RefBookItem(models.Model):
    # элемент справочника
    ref_book = models.ForeignKey(ReferenceBook, related_name='item', on_delete=models.CASCADE)
    article = models.CharField(max_length=50)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.id)

