# Generated by Django 5.0.3 on 2024-03-26 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.book')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.book')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.book')),
                ('passages', models.ManyToManyField(related_name='test_passages', to='admin_panel.passage')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.unit')),
            ],
        ),
        migrations.AddField(
            model_name='passage',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.unit'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=40, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id', 'chat_id'], name='admin_panel_id_57c39f_idx'), models.Index(fields=['-created_at'], name='admin_panel_created_3a7938_idx')],
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='images/nophoto.jpg', upload_to='images/%Y/%m/%d')),
                ('image_url', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.user')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=500)),
                ('definition', models.CharField(max_length=500)),
                ('translated', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.book')),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.passage')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.unit')),
            ],
            options={
                'ordering': ['word'],
            },
        ),
        migrations.CreateModel(
            name='VocabularyTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.SmallIntegerField(default=0)),
                ('correct', models.SmallIntegerField(default=0)),
                ('wrong', models.SmallIntegerField(default=0)),
                ('result', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.user')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
