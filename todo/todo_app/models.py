from django.db import models

class todo_item(models.Model):
    owner = models.CharField(max_length=500)
    created_at = models.DateTimeField('date published')
    completed = models.BooleanField()
    content = models.CharField(max_length=500)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.content

