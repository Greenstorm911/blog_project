from django.db import models
from django.contrib.auth.models import User

class articale(models.Model):
    #writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.body[0:30]}"
    
