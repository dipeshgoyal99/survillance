from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.IntegerField(max_length=12, null=True)
    address = models.CharField(max_length=255, null=True)
    def save(self, *args,**kwargs):
        self.username = self.email
        return super(User, self).save(**args, **kwargs)

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name