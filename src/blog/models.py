from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
    Title = models.CharField(max_length = 200)
    Text = models.TextField() 
    Author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)  
    Created_date = models.DateTimeField(auto_now=True, null=True) 
    Published_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.Title