from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .producer import publish

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @method_decorator(cache_page(60 * 15))  # Кэширование на 15 минут
    @swagger_auto_schema(
        operation_description="Получить список всех книг",
        responses={200: BookSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        publish(method='list', body={'message': 'Books list requested'})
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))  # Кэширование на 15 минут
    @swagger_auto_schema(
        operation_description="Получить книгу по ID",
        responses={200: BookSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        book_id = kwargs.get('pk', None)
        publish(method='retrieve', body={'message': f'Book {book_id} retrieved'})
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать новую книгу",
        request_body=BookSerializer,
        responses={201: BookSerializer},
    )
    def create(self, request, *args, **kwargs):
        publish(method='create', body={'message': 'New book created', 'data': request.data})
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить книгу по ID",
        request_body=BookSerializer,
        responses={200: BookSerializer},
    )
    def update(self, request, *args, **kwargs):
        book_id = kwargs.get('pk', None)
        publish(method='update', body={'message': f'Book {book_id} updated', 'data': request.data})
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить книгу по ID",
        responses={204: openapi.Response('Книга успешно удалена')},
    )
    def destroy(self, request, *args, **kwargs):
        book_id = kwargs.get('pk', None)
        publish(method='destroy', body={'message': f'Book {book_id} deleted'})
        return super().destroy(request, *args, **kwargs)
