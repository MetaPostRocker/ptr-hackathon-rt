# Generated by Django 4.2.6 on 2023-10-14 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical_tests', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalcertificate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='medicalcertificate',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_tests.medicalcertificatetype', verbose_name='Certificate type'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='medicalcertificate',
            order_with_respect_to='owner',
        ),
    ]
