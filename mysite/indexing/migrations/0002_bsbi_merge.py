# Generated by Django 2.1.1 on 2018-12-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BSBI_Merge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('documents', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]