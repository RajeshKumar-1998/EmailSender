# Generated by Django 3.0.6 on 2020-05-31 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.TextField(max_length=10000)),
                ('mes', models.TextField(max_length=100000)),
            ],
            options={
                'get_latest_by': 'id',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_mail', models.EmailField(max_length=300)),
                ('to_mail', models.EmailField(max_length=300)),
            ],
            options={
                'verbose_name': 'users',
                'verbose_name_plural': 'users',
            },
        ),
    ]
