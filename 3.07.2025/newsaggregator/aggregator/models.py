from django.db import models

class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title