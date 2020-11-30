from django.db import models


# Create your models here.

class Glossary(models.Model):
    # справочник
    VERSIONS = (
        ('0.1', '1'),
        ('0.2', '2'),
        ('0.3', '3'),
    )
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    description = models.TextField()
    version = models.CharField(max_length=10, choices=VERSIONS)
    initial_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.short_name)


class GlossaryItem(models.Model):
    # элемент справочника
    ref_book = models.ForeignKey(Glossary, related_name='item', on_delete=models.CASCADE)
    article = models.CharField(max_length=50)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.id)

