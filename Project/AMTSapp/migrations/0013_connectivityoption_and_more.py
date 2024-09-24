# Generated by Django 5.0.7 on 2024-09-14 04:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMTSapp', '0012_remove_software_software_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectivityOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='computerhardware',
            name='account_head',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='computerhardware',
            name='date_of_purchase',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='computerhardware',
            name='stock_register_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='projector',
            name='ASSET_ID',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='projector',
            name='account_head',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projector',
            name='brand',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.RemoveField(
            model_name='projector',
            name='connectivity',
        ),
        migrations.AlterField(
            model_name='projector',
            name='contrast_ratio',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='projector',
            name='date_of_purchase',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='projector',
            name='location',
            field=models.CharField(choices=[('isl_lab', 'ISL Lab'), ('cc_lab', 'CC Lab'), ('project_lab', 'Project Lab'), ('ibm_lab', 'IBM Lab'), ('g1_class_first_year', 'G1 Class First Year'), ('g1_class_second_year', 'G1 Class Second Year'), ('g2_class_first_year', 'G2 Class First Year'), ('g2_class_second_year', 'G2 Class Second Year'), ('wireless_communication_lab', 'Wireless Communication Laboratory'), ('library', 'Library')], max_length=50),
        ),
        migrations.AlterField(
            model_name='projector',
            name='model',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='projector',
            name='resolution',
            field=models.CharField(choices=[('480p', '480p'), ('720p', '720p'), ('1080p', '1080p'), ('4K', '4K')], max_length=10),
        ),
        migrations.AlterField(
            model_name='projector',
            name='stock_register_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='projector',
            name='type_of_asset',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='projector',
            name='connectivity',
            field=models.ManyToManyField(to='AMTSapp.connectivityoption'),
        ),
    ]