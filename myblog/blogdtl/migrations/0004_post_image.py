# Generated by Django 3.2.5 on 2023-02-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdtl', '0003_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
