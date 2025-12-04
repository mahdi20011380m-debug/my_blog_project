from django.db import models  
  
# Create your models here.  
class user(models.Model):  
    username = models.CharField(max_length=200)  
    password = models.CharField(max_length=200)  
    creat_at = models.DateTimeField(auto_now_add=True)  
    last_login = models.DateTimeField(null=True , blank=True)  
  
    def __str__(self):  
        return f"user(username={self.username})"  