# Generated by Django 2.2.3 on 2019-07-11 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_id', models.CharField(max_length=340)),
                ('goal_name', models.CharField(max_length=340)),
                ('created_by', models.CharField(max_length=340)),
                ('moved_by', models.CharField(max_length=340)),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='akinwunmi_nathanielscrumy.GoalStatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrumy_goals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_from', models.CharField(max_length=340)),
                ('moved_to', models.CharField(max_length=340)),
                ('created_by', models.CharField(max_length=340)),
                ('moved_by', models.CharField(max_length=340)),
                ('time_of_action', models.TimeField(max_length=340)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akinwunmi_nathanielscrumy.ScrumyGoals')),
            ],
        ),
    ]
