from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return(self.user.username)
def createProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(createProfile,sender=User)