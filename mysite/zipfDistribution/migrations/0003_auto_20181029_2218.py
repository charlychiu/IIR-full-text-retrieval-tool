# Generated by Django 2.1.1 on 2018-10-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zipfDistribution', '0002_porterindextwitter_rawindextwitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='porterindex',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='porterindextwitter',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rawindex',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rawindextwitter',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
    ]
