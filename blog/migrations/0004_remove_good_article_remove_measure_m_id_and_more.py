# Generated by Django 4.0.6 on 2022-07-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_good_title_alter_measure_m_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='article',
        ),
        migrations.RemoveField(
            model_name='measure',
            name='m_id',
        ),
        migrations.RemoveField(
            model_name='store',
            name='store_id',
        ),
        migrations.AlterField(
            model_name='store',
            name='store_name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
