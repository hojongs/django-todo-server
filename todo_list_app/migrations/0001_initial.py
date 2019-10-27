# Generated by Django 2.2.6 on 2019-10-27 01:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('parent_todo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_list_app.Todo')),
            ],
        ),
    ]
