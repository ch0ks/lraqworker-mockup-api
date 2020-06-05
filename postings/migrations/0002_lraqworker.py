# Generated by Django 3.0.7 on 2020-06-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LRAQWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saId', models.CharField(help_text='Required.', max_length=10, unique=True, verbose_name='SA GUS Id')),
                ('surveyLink', models.CharField(help_text='URL to the Survey', max_length=10, verbose_name='Survey Link')),
                ('surveyId', models.CharField(help_text='Required. Example: SA-000002', max_length=10, unique=True, verbose_name='SA Number')),
            ],
        ),
    ]
