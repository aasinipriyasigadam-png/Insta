from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_id=models.ForeignKey(User,on_delete = models.DO_NOTHING)
    display_name=models.CharField(null=True,max_length=100)
    bio=models.CharField(null=True,max_length=100)
    avatar=models.ImageField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class Post(models.Model):
    VISIBILITY={
        "pb":"public",
        "fol":"followers"
    }    
    user_id=models.ForeignKey(User,on_delete = models.DO_NOTHING)
    media_file=models.FileField()
    media_type=models.CharField()
    caption=models.CharField(max_length=5000)
    visibility=models.CharField(max_length=3,
                                choices=VISIBILITY,
                                default="followers")
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)


class Follow(models.Model):
    follower_id=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="follower_id")
    following_id=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="following_id")
    created_at=models.DateTimeField(auto_now=True)

class Conversation(models.Model):
    created_at=models.DateTimeField(auto_now=True)

class ConversationParticipant(models.Model):
    conversation_id=models.ForeignKey(User,on_delete = models.DO_NOTHING,related_name="conversation_id")
    user_id=models.ForeignKey(User,on_delete = models.DO_NOTHING,related_name="user_id")
    joined_at=models.DateTimeField(auto_now=True)
    last_read_at=models.DateTimeField(auto_now=True)

class Message(models.Model):
    message_conversation_id=models.ForeignKey(User,on_delete = models.DO_NOTHING,related_name="message_conversation_id")
    sender_id=models.ForeignKey(User,on_delete = models.DO_NOTHING,related_name="sender_id")
    text=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    edited_at=models.DateTimeField(auto_now=True)












