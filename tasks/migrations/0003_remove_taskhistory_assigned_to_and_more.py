# Generated by Django 4.2.1 on 2023-05-09 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_rename_przypisany_uzytkownik_task_assigned_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskhistory',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='assigned_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='status',
            field=models.CharField(choices=[('Nowy', 'Nowy'), ('W toku', 'W toku'), ('Rozwiązany', 'Rozwiązany')], default='Nowy'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
