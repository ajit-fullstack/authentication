# Generated by Django 4.0.1 on 2024-03-10 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_page_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('panna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.page')),
                ('likes', models.IntegerField()),
            ],
            bases=('myapp.page',),
        ),
    ]