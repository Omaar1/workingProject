# Generated by Django 2.0.4 on 2018-04-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_product_doc_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='fuckoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('filetype', models.CharField(max_length=120)),
            ],
        ),
    ]
