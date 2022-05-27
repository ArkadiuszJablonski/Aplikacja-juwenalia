from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime

class LostItem(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(max_length=500)
    kontakt = models.CharField(max_length=255)
    data_dodania = models.DateTimeField(default=datetime.now)
    isAccepted = models.BooleanField(default=False)
    acceptedBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='accepted_by', blank=True, null=True)
    isLost = models.BooleanField(default=False)
    zdjecie = models.ImageField(blank=True, upload_to='biuro_pics/%Y/%m/%d/', default = 'default_biuro.jpg')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        super(LostItem, self).save(*args, **kwargs)

        img = Image.open(self.zdjecie.path)
        output_size = (400, 400)
        img.thumbnail(output_size)
        img.save(self.zdjecie.path)