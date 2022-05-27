from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    tytul = models.CharField(max_length=100)
    tresc = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now_add=True <- we can't modify the data // auto_now <- update time
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tytul
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Photo(models.Model):
    opis = models.CharField(max_length=20)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    zdjecie = models.ImageField(null=False, blank=False, width_field='width', height_field='height', upload_to='gallery_pics')
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.opis

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('photo-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date_posted']