# Generated by Django 3.1 on 2021-03-22 00:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[('movie', 'фильм'), ('tv_show', 'шоу')], max_length=20, verbose_name='тип')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('description', models.TextField(blank=True, verbose_name='содержание')),
                ('creation_date', models.DateField(blank=True, verbose_name='дата создания')),
                ('age_rating', models.TextField(blank=True, verbose_name='возрастной ценз')),
                ('link', models.URLField(blank=True, verbose_name='ссылка на файл')),
            ],
            options={
                'verbose_name': 'кинопроизведение',
                'verbose_name_plural': 'кинопроизведения',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[('director', 'режиссер'), ('actor', 'актер'), ('writer', 'сценарист')], max_length=20, verbose_name='тип')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='фамилия')),
                ('film', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
