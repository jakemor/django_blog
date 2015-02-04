from django.db import models
from django.contrib.auth.models import User

class todo_item(models.Model):
    # owner = models.ForeignKey(User)
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField('date published')
    completed = models.BooleanField()
    content = models.CharField(max_length=500)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.content

