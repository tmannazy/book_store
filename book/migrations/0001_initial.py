# Generated by Django 4.1.3 on 2022-11-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=20)),
                ('date_published', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('edition', models.PositiveSmallIntegerField()),
                ('genre', models.CharField(choices=[('C', 'Comedy'), ('T', 'Tragedy'), ('TC', 'Tragicomedy'), ('H', 'Horror'), ('CR', 'Crime'), ('R', 'Romance'), ('SF', 'Sci-Fi')], default='R', max_length=2)),
            ],
        ),
    ]