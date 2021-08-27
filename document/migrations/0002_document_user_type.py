# Generated by Django 3.2 on 2021-08-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user_type',
            field=models.CharField(choices=[('talimga_oid', 'talimga_oid'), ('vazirlar_mahkamasi', 'vazirlar_mahkamasi'), ('prezident_farmoni', 'prezident_farmoni'), ('boshqarma_boshligi', 'boshqarma_boshligi'), ('xalq_talim_vaziri', 'xalq_talim_vaziri')], default='talimga_oid', max_length=20),
        ),
    ]