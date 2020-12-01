from django.db import models


class Glossary(models.Model):
    # справочник
    name = models.CharField(max_length=255, verbose_name="наименование")
    short_name = models.CharField(max_length=50, verbose_name='короткое имя')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = "справочник "

    def __str__(self):
        return '{}'.format(self.short_name)


class Version(models.Model):
    glossary = models.ForeignKey(Glossary, on_delete=models.CASCADE, verbose_name="справочник")
    version = models.CharField(max_length=10, verbose_name='версия справочника')
    initial_date = models.DateField(verbose_name="дата действия")

    class Meta:
        verbose_name = "Версии "
        unique_together = (
            'glossary',
            'version',
        )
    def __str__(self):
        return '{} версии - {}'.format(self.glossary.name, self.version)


class GlossaryItem(models.Model):
    # элемент справочника
    ref_book = models.ForeignKey(Version, related_name='item',
                                 on_delete=models.CASCADE, verbose_name="справочник")
    article = models.CharField(max_length=50, verbose_name="артикл")
    value = models.CharField(max_length=255, blank=True, verbose_name="значение")

    class Meta:
        verbose_name = "элементы справочника "

    def __str__(self):
        return '{}'.format(self.article)
