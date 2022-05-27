from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Koncert(models.Model):
    KONCERTY = 'KO'
    T_KULTURY = 'TK'
    T_SPORTU = 'TS'
    TYG_TEM = (
        (T_KULTURY,'Tydzień Kultury i Nauki'),
        (T_SPORTU,'Tydzień Sportu'),
        (KONCERTY,'Koncerty'),
    )
    nazwa_wydarzenia= models.CharField(max_length=100)
    opis = models.TextField(max_length=500)
    data_start = models.DateTimeField(default='2019-00-00 00:00:00')
    data_koniec = models.DateTimeField(default='2019-00-00 00:00:00')
    miejsce_wydarzenia = models.CharField(max_length=20)
    organizator = models.ForeignKey(User, on_delete=models.CASCADE)
    uczestnicy = models.ManyToManyField(User, blank = True, related_name='participants')
    rodzaj_wydarzenia = models.CharField(choices=TYG_TEM,max_length=2, default=KONCERTY)
    zdjecie = models.ImageField(default = 'default.jpg', upload_to='koncert_pics')

    def __str__(self):
        return self.nazwa_wydarzenia

    def get_absolute_url(self):
        return reverse('koncerty-detail', kwargs={'pk': self.pk})

    @classmethod
    def take_part(cls, user, pk):
        koncert = cls.objects.get(pk=pk)
        koncert.uczestnicy.add(user)

    @classmethod
    def remove_participation(cls, user,pk):
        koncert = cls.objects.get(pk=pk)
        koncert.uczestnicy.remove(user)

    def save(self, *args, **kwargs):
        super(Koncert, self).save(*args, **kwargs)
