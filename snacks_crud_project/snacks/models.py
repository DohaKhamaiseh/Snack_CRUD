from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=255)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    desc = models.TextField(default='How your snack was? ^_^')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('snacks')