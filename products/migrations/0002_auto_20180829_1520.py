from __future__ import unicode_literals
from django.db import migrations


def create_initial_products(apps, schema_editor):
    Product = apps.get_model('products', 'Product')

    Product(name='Samsung TV', description='42" Samsung Digital Tv', price=56000).save()
    Product(name='Lenovo Laptop', description='Lenovo T450 Slim', price=143000).save()
    Product(name='Sony PS4 PlayStation', description='Sony PS4 PlayStation', price=43000).save()
    Product(name='Iphone X', description='Apple Iphone X 128gb', price=125000).save()
    Product(name='Samsung S9', description='Samsung S9 Smartphone', price=96000).save()
    Product(name='Cantucci', description='Cantucci di Prato almond biscuits.', price=40).save()
    Product(name='Xperia XZ2', description='Sony Xperia XZ2 64gb Smartphone', price=65000).save()
    Product(name='Rolex Air King', description='Rolex Air King Men Watch', price=298508.73).save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_products),
    ]