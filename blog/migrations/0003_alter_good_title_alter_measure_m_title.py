# Generated by Django 4.0.6 on 2022-07-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_good_measure_order_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='measure',
            name='m_title',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]