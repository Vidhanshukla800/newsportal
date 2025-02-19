# Generated by Django 4.1 on 2022-09-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_city_ncategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntitle', models.CharField(max_length=500)),
                ('nhead', models.CharField(max_length=500)),
                ('ndes', models.TextField()),
                ('npic', models.ImageField(null=True, upload_to='static/news/')),
                ('ndate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpic', models.ImageField(upload_to='static/trending/')),
                ('thead', models.CharField(max_length=300)),
                ('tdate', models.DateField()),
                ('tdes', models.TextField()),
            ],
        ),
    ]
