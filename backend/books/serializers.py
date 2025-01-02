from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


    def validate_published_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Дата публикации не может быть в будущем.")
        return value
