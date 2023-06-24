from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=50,verbose_name='نام کتاب')
    writer = models.CharField(max_length=60,verbose_name='نویسنده')
    summary = models.TextField(verbose_name='خلاصه')
    year = models.PositiveSmallIntegerField(verbose_name='سال انتشار')
    pages = models.PositiveSmallIntegerField(verbose_name='تعداد صفحات')
    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
