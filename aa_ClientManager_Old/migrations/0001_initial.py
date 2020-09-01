# Generated by Django 3.1 on 2020-08-29 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='backlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date_beg', models.DateField(auto_now_add=True)),
                ('date_end', models.DateField()),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=100)),
                ('sort_of_book', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nif', models.IntegerField()),
                ('date_birth', models.DateField()),
                ('mail', models.EmailField(max_length=100)),
            ],
        ),
    ]
