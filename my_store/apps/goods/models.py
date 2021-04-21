from django.db import models
import datetime


class Good(models.Model):
    UNITS = (
        (1, 'шт.'),
        (2, 'кг.'),
    )

    good_name = models.CharField(verbose_name='наименование товара', max_length=150)
    date_receipt = models.DateField(verbose_name='дата поступления', default=datetime.datetime.now())
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=0, default=0)
    unit = models.IntegerField(verbose_name='единица измерения', choices=UNITS, default=UNITS[0])
    supplier = models.CharField(verbose_name='имя поставщика', max_length=256, blank=True)

    def __str__(self):
        return self.good_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
