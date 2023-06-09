# Generated by Django 4.2.1 on 2023-06-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('describtion', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
                ('prod_img', models.ImageField(blank=True, default='CyberCowboys_auto_x2.jpg', null=True, upload_to='')),
            ],
        ),
    ]
