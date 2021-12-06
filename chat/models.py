from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author.username
    
    def last_25_messages():
        return Message.objects.order_by('-timestamp').all()[:25]


# class Room(models.Model):
#     name = models.CharField(max_length=25)
#     user1 = models.ForeignKey(User, on_delete=models.CASCADE)
#     user2 = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name