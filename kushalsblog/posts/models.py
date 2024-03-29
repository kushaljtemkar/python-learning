from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')

    def body_limited(self):
        return self.body[:100]
