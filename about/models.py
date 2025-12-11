from django.db import models

# Create your models here.
class About(models.Model):
    titleField = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    contentField = models.TextField()

    def __str__(self):
        return self.titleField
