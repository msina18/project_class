# Generated by Django 5.0.6 on 2024-06-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='X',
            field=models.CharField(default='#', max_length=220),
        ),
        migrations.AddField(
            model_name='agent',
            name='descriptions',
            field=models.TextField(default='#'),
        ),
        migrations.AddField(
            model_name='agent',
            name='email',
            field=models.EmailField(default='@', max_length=254),
        ),
        migrations.AddField(
            model_name='agent',
            name='facebook',
            field=models.CharField(default='#', max_length=220),
        ),
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.ImageField(default='1.jpg', upload_to='property'),
        ),
        migrations.AddField(
            model_name='agent',
            name='instegram',
            field=models.CharField(default='#', max_length=220),
        ),
        migrations.AddField(
            model_name='agent',
            name='linkdin',
            field=models.CharField(default='#', max_length=220),
        ),
        migrations.AddField(
            model_name='agent',
            name='phon',
            field=models.IntegerField(default='0918'),
        ),
    ]
