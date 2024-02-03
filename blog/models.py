from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

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
    slug = models.SlugField(unique=True, blank=True, null=True)
    class Meta:
        ordering = ['date']
        verbose_name = 'POST'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'slug':self.slug})

    
    def __str__(self):
        return f"{self.title} - {self.body[0:30]}"
    
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=25)
    meli_code = models.IntegerField()
    image = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username