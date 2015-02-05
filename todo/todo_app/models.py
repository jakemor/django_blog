from django.db import models
from django.contrib.auth.models import User

class todo_item(models.Model):
    # owner = models.ForeignKey(User)
    owner = models.ForeignKey(User)
    created_at = models.DateTimeFielddate = models.DateTimeField(auto_now_add=True, blank=True)
    completed = models.BooleanField(default = False)
    content = models.CharField(max_length=500)
    completed_at = models.DateTimeFielddate = models.DateTimeField(auto_now_add=True, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.content

