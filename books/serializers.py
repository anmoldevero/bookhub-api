from rest_framework import serializers

from .models import Book, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'pdf_content' ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = ['comment']



