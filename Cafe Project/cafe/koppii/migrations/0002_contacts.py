# Generated by Django 4.1.5 on 2023-03-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koppii', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=50)),
            ],
        ),
    ]
