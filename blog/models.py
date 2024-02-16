from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from openai import OpenAI
import socket

class Category(models.Model):
    title = models.CharField(max_length=50)   
    date = models.DateField(auto_now=True) 
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
class articale(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    image = models.ImageField(upload_to="images/", verbose_name='عکس')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    descryption = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    slug = models.SlugField(unique=True, blank=True, null=True)
    genrate_descryption = models.BooleanField(default=False, verbose_name='تولید توضیحات')
    class Meta:
        ordering = ['date']
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
    def save(self, *args, **kwargs):
        if self.genrate_descryption:
            try:
                self.descryption = send_message(self.title)
                self.genrate_descryption = False
            except Exception as e:
                print(f'error {e}')
        self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'slug':self.slug})

    
    def __str__(self):
        return f"{self.title} - {self.descryption[0:30]}"
    def short_text(self):
        return self.descryption[0:30]
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=25)
    meli_code = models.IntegerField()
    image = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'پروفایل کاربری'
        verbose_name_plural = 'پروفایل کاربری ها'
def send_message(message):
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_address = ('38.54.61.158', 9999)  

    try:
        sender_socket.connect(sender_address)
        sender_socket.sendall(message.encode('utf-8'))
        print(f"Sent message: {message}")

        # Receive the modified string back from the receiver
        modified_message = sender_socket.recv(1024)
        print(f"Modified message received: {modified_message.decode('utf-8')}")

    finally:
        sender_socket.close()

    return modified_message.decode('utf-8')
    