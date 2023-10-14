# Generated by Django 4.2.6 on 2023-10-14 06:10

from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical_institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalCertificateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MedicalCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=pathlib.PureWindowsPath('C:/Users/Lenovo/PycharmProjects/president_tech_award/core/media'), verbose_name='File')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('received_date', models.DateTimeField(verbose_name='Received date')),
                ('expiration_date', models.DateTimeField(verbose_name='Expiration date')),
                ('given_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical_institutions.medicalinstitution', verbose_name='Given by')),
            ],
        ),
    ]
