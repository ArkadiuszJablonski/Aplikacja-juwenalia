from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

KATEGORIE = (
    ('testowe', 'testowe'),
    ('Przypomnienie o wydarzeniu', 'Przypomnienia'),
    ('Ważne informacje', 'Ważne'),
    ('Konkursy', 'Konkurs'),
    ('Inne', 'Inne') 
)

ODBIORCY = (
    ('wszyscy', 'Wszyscy'),
    ('Brak uczelni', 'Brak uczelni'),
    ('Politechnika Rzeszowska', 'Politechnika Rzeszowska'),
    ('Uniwersytet Rzeszowski', 'Uniwersytet Rzeszowski'),
    ('Inna uczelnia', 'Inna uczelnia')
)


class Powiadomienie(models.Model):
    nazwa = models.CharField(max_length=100)
    treść = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    kategoria = models.CharField(max_length=40, choices=KATEGORIE, default='testowe')
    odbiorcy = models.CharField(max_length=40, choices=ODBIORCY, default='Wszyscy')
        
    def __str__(self):
        return self.nazwa
    
    def get_absolute_url(self):
        return reverse('powiadomienie-detail', kwargs={'pk': self.pk})