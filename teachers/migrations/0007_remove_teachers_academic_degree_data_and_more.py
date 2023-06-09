# Generated by Django 4.1.5 on 2023-04-20 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_languagecert_remove_teachers_academic_degree_test_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='academic_degree_data',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='academic_rank_data',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='language_cert',
        ),
        migrations.AddField(
            model_name='academicdegreedata',
            name='academic_degree_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='academic_degree_data_name', to='teachers.academicdegreedata'),
        ),
        migrations.AddField(
            model_name='academicrankdata',
            name='academic_rank_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='academic_rank_data_name', to='teachers.academicrankdata'),
        ),
        migrations.AddField(
            model_name='languagecert',
            name='language_cert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language_cert_name', to='teachers.languagecert'),
        ),
    ]
