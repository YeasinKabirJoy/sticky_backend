from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


class Note(models.Model):
    board = models.ForeignKey(Board,related_name='notes',on_delete=models.CASCADE,null=True)
    body = models.TextField(blank=True,null=True)
    colors = models.CharField(max_length=200)
    position = models.CharField(max_length=50)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)