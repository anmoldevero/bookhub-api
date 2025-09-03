from rest_framework import serializers
from . models import Book, Like, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = '__all__'



