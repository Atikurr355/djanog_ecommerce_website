from django.db import models


class About(models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to="About_image")

    def __str__(self):
        return self.desc
