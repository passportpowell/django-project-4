# Generated by Django 3.2.17 on 2023-02-23 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_event_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='accepted',
            new_name='approved',
        ),
    ]
