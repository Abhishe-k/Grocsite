# Generated by Django 4.0.1 on 2022-02-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_remove_client_fullname_client_phone_item_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(choices=[('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')], default='CH', max_length=2),
        ),
    ]
