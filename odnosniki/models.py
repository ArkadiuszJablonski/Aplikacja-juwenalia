from django.db import models
from PIL import Image
from django.urls import reverse

class Odnosnik(models.Model):
    nazwa = models.CharField(max_length=20)
    link = models.TextField()
    zdjecie = models.ImageField(null=False, upload_to='odnosniki_pics')

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('odnosniki-home')

    def save(self, *args, **kwargs):
        super(Odnosnik, self).save(*args, **kwargs)

        img = Image.open(self.zdjecie.path)
        img.save(self.zdjecie.path)