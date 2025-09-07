from rest_framework import serializers
from . models import Book, Like, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'pdf_content' ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = ['comment']



