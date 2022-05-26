# Generated by Django 4.0.4 on 2022-05-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('dateOfBirth', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]