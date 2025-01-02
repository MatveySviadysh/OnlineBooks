from djongo import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    publication_date = models.DateField(verbose_name="Дата публикации", blank=True, null=True)
    
    genre = models.CharField(max_length=100, verbose_name="Жанр", blank=True, null=True)
    isbn = models.CharField(max_length=13, verbose_name="ISBN", unique=True, blank=True, null=True)

    pages = models.PositiveIntegerField(verbose_name="Количество страниц", blank=True, null=True)
    language = models.CharField(max_length=50, verbose_name="Язык", blank=True, null=True)
    publisher = models.CharField(max_length=255, verbose_name="Издательство", blank=True, null=True)

    cover_image = models.ImageField(upload_to="book_covers/", verbose_name="Обложка книги", blank=True, null=True)
    available = models.BooleanField(default=True, verbose_name="Доступна для заказа")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']

    def __str__(self):
        return f"{self.title} — {self.author}"
