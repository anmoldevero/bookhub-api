from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import Book, Like, Comment
from.serializers import BookSerializer,CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Count



class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.annotate(likes_count=Count("likes"))
    
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['author', 'title']
    ordering_fields = ['created_at']
    ordering = ['-likes_count']

    
    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        book = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, book=book)
        if not created:
            return Response({"detail": "Already liked"}, status=400)
        return Response({"detail": "Book liked successfully"})
    
    @action(detail=True, methods=['get'])
    def likes(self, request, pk):
        book = self.get_object()
        likes = book.likes.all()   
        return Response({"total_likes": likes.count()})
    


    @action(detail=True, methods=['post'])
    def comment(self, request, pk):
        book = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save(user=request.user, book=book)
        return Response({"detail": "Comment added", "comment": CommentSerializer(comment).data})
    
    @action(detail=True, methods=['get'])
    def comments(self, request, pk):
        book = self.get_object()
        comments = book.comments.all()  
        return Response(CommentSerializer(comments, many=True).data)
