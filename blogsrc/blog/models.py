from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	createdAt = models.DateTimeField(auto_now_add=True, blank=True)