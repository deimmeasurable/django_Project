# Generated by Django 4.0.4 on 2022-04-27 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('natives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.TextField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('natives', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='natives.native')),
            ],
        ),
    ]
