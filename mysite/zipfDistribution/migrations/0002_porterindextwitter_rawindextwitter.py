# Generated by Django 2.1.1 on 2018-10-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zipfDistribution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PorterIndexTwitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contents', models.ManyToManyField(to='zipfDistribution.Content')),
            ],
        ),
        migrations.CreateModel(
            name='RawIndexTwitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contents', models.ManyToManyField(to='zipfDistribution.Content')),
            ],
        ),
    ]
