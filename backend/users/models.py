from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile (AbstractUser):
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField(max_length=50,blank=True,null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    #image=models.ImageField(blank=True, null=True)

    groups = models.ManyToManyField('auth.Group',related_name='user_profiles',blank=True,verbose_name='groups',help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',)
    user_permissions = models.ManyToManyField('auth.Permission',related_name='user_profiles',blank=True,verbose_name='user permissions',help_text='Specific permissions for this user.',)

    def __str__(self):
        return self.username

class Like(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post=models.ForeignKey("posts.Post",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.post.pk}"
    
class Save(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post=models.ForeignKey("posts.Post",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.post.pk}"

class Follower (models.Model):
    follower=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='followers_set')
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='followed')

    def __str__(self):
        return f"{self.follower.username} follows  {self.user.username}"