# Generated by Django 3.2.6 on 2021-08-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imge',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
