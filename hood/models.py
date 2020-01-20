from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.   
class Admin(models.Model):
   name = models.CharField(max_length =30)
   def __str__(self):
      return self.name
  
class Hood(models.Model):
   admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
   name = models.CharField(max_length =30)
   location = models.CharField(max_length =30)
   occupants_count = models.IntegerField()
   
   def __str__(self):
      return self.name
   
   def create_hood(self):
      """
      Create a new neighbourhood to the database    
      """
      self.save()  
      
   def delete_hood(self):
      """
      Create a new neighbourhood to the database    
      """
      self.delete()    
   
   def update_hood(self):
      """
      function to update some properties of the hood class
      """
      self.hood.update()   
      
   @classmethod
   def find_hood(hood_id):
      """
      function to search a hood by use of the hood-id
      """
      hood = cls.objects.filter(id__contains=hood_id)
      return hood      
   
class User(AbstractUser):
   name = models.CharField(max_length =30)
   hood = models.OneToOneField(Hood, on_delete=models.CASCADE, null=True)
   email = models.CharField(max_length =30)
   
      
class Business(models.Model):
   name = models.CharField(max_length =30)
   hood = models.ForeignKey(Hood,on_delete=models.CASCADE, default = 1)
   biz_email =  models.CharField(max_length =30)
   
class Post(models.Model):
   title = models.CharField(max_length=100)
   content = models.TextField()
   date_posted = models.DateTimeField(default=timezone.now)
   author = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.title  
   
   def get_absolute_url(self):
      return reverse('post-detail', kwargs={'pk': self.pk}) 