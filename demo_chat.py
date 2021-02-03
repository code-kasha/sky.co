from django.db import models
 
from apps.accounts.models import UserProfile
 
 
class Message(models.Model):
""" The container for storing actual messages """
    author = models.ForeignKey( 
	UserProfile, 
	related_name="messages", 
	on_delete=models.CASCADE
	)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_flagged = models.BooleanField(default=False)
 
    def __str__(self):
        return self.content[:10]
 
 
class Conversation(models.Model):
""" The container for storing direct messages between two people """
    person1 = models.ForeignKey(
	UserProfile, 
	on_delete=models.CASCADE, 
	related_name="dm_one"
	)
    person2 = models.ForeignKey(
	UserProfile, 
	on_delete=models.CASCADE, 
	related_name="dm_two"
	)
    messages = models.ManyToManyField(
	Messages, 
	related_name="dm_messages",
	blank=True
	)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_flagged = models.BooleanField(default=False)
 
    def __str__(self):
        return f"{self.reciever} - {self.sender}"
 
 
class ChatRoom(models.Model):
""" The container for storing Room Based chat messages """
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(max_length=400)
    members = models.ManyToManyField(
		UserProfile,
		related_name="rooms",
		blank=True
		)
    messages = models.ManyToManyField(
		Message, 
		related_name="room_messages", 
		blank=True
		)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_flagged = models.BooleanField(default=False)
 
    def __str__(self):
        return f"{self.title}"
 
# I want to know if I'm using django models correctly for my situation here,
# I want to handle the actual sending/receiving using JS and probably socket.io
