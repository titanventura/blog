# Generated by Django 2.2.6 on 2019-10-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('read_time', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('image', models.URLField(null=True)),
            ],
        ),
    ]
