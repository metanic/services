# Generated by Django 2.1b1 on 2018-07-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180705_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, editable=False, related_name='categories', to='posts.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(blank=True, editable=False, related_name='posts', to='posts.Topic'),
        ),
    ]
