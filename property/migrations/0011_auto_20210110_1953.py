# Generated by Django 2.2.4 on 2021-01-10 16:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20210109_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='owner_deprecated',
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]