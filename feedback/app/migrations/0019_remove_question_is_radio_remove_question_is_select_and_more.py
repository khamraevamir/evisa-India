# Generated by Django 4.1.4 on 2022-12-21 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20221219_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='is_radio',
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_select',
        ),
        migrations.AddField(
            model_name='question',
            name='types',
            field=models.CharField(choices=[('1', 'is_text'), ('2', 'is_radio'), ('3', 'is_select'), ('4', 'is_date')], default='1', max_length=2, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='changed_name',
            field=models.BooleanField(default=False, verbose_name='Смена имени'),
        ),
    ]