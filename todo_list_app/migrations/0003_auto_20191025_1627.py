# Generated by Django 2.2.6 on 2019-10-25 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0002_auto_20191025_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='parent_todo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_list_app.Todo'),
        ),
    ]