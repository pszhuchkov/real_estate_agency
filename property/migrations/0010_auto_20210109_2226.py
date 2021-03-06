# Generated by Django 2.2.4 on 2021-01-09 19:26

from django.db import migrations


def copy_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            owner=flat.owner, owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20201231_0028'),
    ]

    operations = [
        migrations.RunPython(copy_owners)
    ]
