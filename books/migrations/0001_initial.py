# Generated by Django 2.2.1 on 2019-05-25 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=20)),
                ('number_of_pages', models.SmallIntegerField()),
                ('release_date', models.DateField()),
                ('authors', models.ManyToManyField(related_name='books', to='books.Author')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.Country')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.Publisher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
