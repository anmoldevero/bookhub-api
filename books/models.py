from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    pdf_content = models.FileField(upload_to='books/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


# Like model
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} Likes {self.book.title}"
    

# Comment model
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        ordering = ['created_at'] 

    def __str__(self): 
        return f"Comment by {self.user.username} on {self.book.title}"
    

