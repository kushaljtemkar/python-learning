from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/")
    body = models.TextField()

    def __str__(self):
        return self.title

    def custom_date(self):
        return self.pub_date.strftime("%b %d %Y")
