# Generated by Django 3.2.5 on 2023-02-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdtl', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
