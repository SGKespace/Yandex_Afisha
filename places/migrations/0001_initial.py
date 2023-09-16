# Generated by Django 3.1.1 on 2023-09-12 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название места')),
                ('description_short', models.CharField(max_length=100, verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Подробное описание')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_image', to='places.place')),
            ],
        ),
    ]
