# Generated by Django 3.2.12 on 2022-02-28 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photos.category'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(),
        ),
    ]
