# Generated by Django 2.2 on 2019-06-23 20:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('uczelnia', models.CharField(choices=[('Brak uczelni', 'Brak uczelni'), ('Politechnika Rzeszowska', 'Politechnika Rzeszowska'), ('Uniwersytet Rzeszowski', 'Uniwersytet Rzeszowski'), ('Inna uczelnia', 'Inna uczelnia')], default='Brak uczelni', max_length=40)),
                ('wydział', models.CharField(blank=True, max_length=100)),
                ('rok', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]