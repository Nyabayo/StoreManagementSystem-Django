# Generated by Django 5.1.5 on 2025-01-22 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp1', '0002_alter_store_created_by_alter_store_issue_by_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Store',
            new_name='Stock',
        ),
    ]
