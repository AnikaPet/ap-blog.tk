# Generated by Django 4.0.1 on 2022-01-25 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(max_length=300)),
                ('body', models.TextField(max_length=3000)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_author', to='cms.author')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
