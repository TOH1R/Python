# Generated by Django 5.1.3 on 2024-12-05 13:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0007_rename_name_blog_title_remove_work_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
