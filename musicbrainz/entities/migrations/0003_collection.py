# Generated by Django 2.2.4 on 2019-08-05 05:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0002_recording'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entity_type', models.TextField()),
                ('_type', models.TextField()),
            ],
        ),
    ]
