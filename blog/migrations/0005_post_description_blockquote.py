# Generated by Django 4.0.4 on 2022-05-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_description_three_ar_post_description_three_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_blockquote',
            field=models.TextField(default='w'),
            preserve_default=False,
        ),
    ]
