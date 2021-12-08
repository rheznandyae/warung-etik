from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

import string
import random


class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(user1=user) | Q(user2=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs

class Room(models.Model):
    name = models.CharField(max_length=25, unique=True)
    user1 = models.ForeignKey(User,related_name='user_1' , on_delete=models.CASCADE)
    user2 = models.ForeignKey(User,related_name='user_2' , on_delete=models.CASCADE)
    
    objects = ThreadManager()
    class Meta:
        unique_together = ['user1', 'user2']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)
        self.name = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        self.name += f'-{self.id}'
        super(Room, self).save(*args, **kwargs)

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.author.username
    
    def last_15_messages(room_name):
        try:
            current_room = Room.objects.get(name=room_name)
            return Message.objects.filter(room=current_room).order_by('timestamp')[:15]
        except Room.DoesNotExist:
            return None
        
    

