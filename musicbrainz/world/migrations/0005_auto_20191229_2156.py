# Generated by Django 2.2.4 on 2019-12-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_auto_20191229_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='_timezone',
            field=models.FloatField(null=True, verbose_name='Timezone'),
        ),
    ]