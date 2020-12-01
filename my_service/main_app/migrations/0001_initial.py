# Generated by Django 2.2.6 on 2020-12-01 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'справочник ',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10)),
                ('initial_date', models.DateField()),
                ('glossary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Glossary')),
            ],
            options={
                'verbose_name': 'Версии ',
                'unique_together': {('glossary', 'version')},
            },
        ),
        migrations.CreateModel(
            name='GlossaryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50)),
                ('value', models.CharField(blank=True, max_length=255)),
                ('ref_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='main_app.Version')),
            ],
            options={
                'verbose_name': 'элементы справочника ',
            },
        ),
    ]
