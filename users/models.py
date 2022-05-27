from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator


UCZELNIE = (
    ('Brak uczelni', 'Brak uczelni'),
    ('Politechnika Rzeszowska', 'Politechnika Rzeszowska'),
    ('Uniwersytet Rzeszowski', 'Uniwersytet Rzeszowski'),
    ('Inna uczelnia', 'Inna uczelnia')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    uczelnia = models.CharField(max_length=40, choices=UCZELNIE, default='Brak uczelni')
    wydział = models.CharField(blank=True, max_length=100)
    rok = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(4), MinValueValidator(1)])
    
    def __str__(self):
        return f'{self.user.username} Profile'
#dopisać usuwanie starych zdjęć profilowych po dodaniu nowego
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
