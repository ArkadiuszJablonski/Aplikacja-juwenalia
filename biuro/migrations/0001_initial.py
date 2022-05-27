# Generated by Django 2.2 on 2019-07-02 20:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField(max_length=500)),
                ('kontakt', models.CharField(max_length=255)),
                ('data_dodania', models.DateTimeField(default=datetime.datetime.now)),
                ('isAccepted', models.BooleanField(default=False)),
                ('isLost', models.BooleanField(default=False)),
                ('zdjecie', models.ImageField(blank=True, default='default_biuro.jpg', upload_to='biuro_pics/%Y/%m/%d/')),
                ('acceptedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accepted_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
