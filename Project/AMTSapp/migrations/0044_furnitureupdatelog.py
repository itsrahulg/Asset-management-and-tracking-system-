# Generated by Django 5.0.7 on 2024-10-14 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMTSapp', '0043_alter_books_location_alter_computerhardware_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureUpdateLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ASSET_ID', models.CharField(max_length=50)),
                ('type_of_furniture', models.CharField(choices=[('Desk', 'Desk'), ('Chair', 'Chair'), ('Cupboard', 'Cupboard'), ('Almirah', 'Almirah'), ('Table', 'Table'), ('Board', 'Board')], max_length=50)),
                ('subtype', models.CharField(choices=[('Desk with Cupboard', 'Desk with Cupboard'), ('Desk without Cupboards', 'Desk without Cupboards'), ('2 Seater Working Table', '2 Seater Working Table'), ('3 Seater Working Table', '3 Seater Working Table'), ('Chair with Study Desk Attached', 'Chair with Study Desk Attached'), ('Wooden chair', 'Wooden Chair'), ('Steel chair', 'Steel Chair'), ('Metal Revolving Chair', 'Metal Revolving Chair'), ('Conference Table', 'Conference Table'), ('Whiteboard', 'Whiteboard'), ('Blackboard', 'Blackboard'), ('Pinboard', 'Pinboard'), ('Noticeboard', 'Noticeboard'), ('Wooden Almirah', 'Wooden Almirah'), ('Steel Almirah', 'Steel Almirah'), ('Wooden Cupboard', 'Wooden Cupboard'), ('Steel Cupboard', 'Steel Cupboard')], max_length=50)),
                ('date_of_purchase', models.DateField()),
                ('account_head', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('ISL Lab', 'ISL Lab'), ('CC Lab', 'CC Lab'), ('Project Lab', 'Project Lab'), ('IBM Lab', 'IBM Lab'), ('K505-Seminar Hall', 'K505-Seminar Hall'), ('Wireless Communication Laboratory', 'Wireless Communication Laboratory'), ('E-learning Center', 'E-learning Center')], max_length=50)),
                ('date_of_update', models.DateField()),
                ('updated_by', models.CharField(max_length=100)),
                ('logged_by', models.CharField(max_length=100)),
                ('furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMTSapp.furniture')),
            ],
        ),
    ]