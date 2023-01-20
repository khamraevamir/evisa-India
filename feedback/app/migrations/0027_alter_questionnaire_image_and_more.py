# Generated by Django 4.0.6 on 2023-01-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_rename_title_ru_question_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото:'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='passport_image',
            field=models.ImageField(blank=True, null=True, upload_to='passport_images/', verbose_name='Фото паспорта:'),
        ),
    ]
