# Generated by Django 4.2.3 on 2023-08-08 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery_app', '0002_category_product_delete_groceryitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
