from django.db import models


class Book(models.Model):
    title = models.CharField(
        'title',
        max_length=100
    )
    author = models.CharField('author', max_length=100)
    pub_year = models.DateField(
        'publication year',
    )
    isbn = models.CharField('isbn', max_length=13)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['pub_year']
