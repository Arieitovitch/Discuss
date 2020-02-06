from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=100, default='hockey')

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=10000)

