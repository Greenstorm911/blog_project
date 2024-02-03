from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)   
    date = models.DateField(auto_now=True) 
    def __str__(self):
        return self.title
    
    
class articale(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    descryption = models.TextField()
    
    
    def __str__(self):
        return f"{self.title} - {self.body[0:30]}"
    
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=25)
    meli_code = models.IntegerField()
    image = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username