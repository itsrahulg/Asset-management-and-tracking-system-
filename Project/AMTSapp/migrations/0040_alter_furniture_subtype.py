# Generated by Django 5.0.7 on 2024-10-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMTSapp', '0039_alter_furniture_subtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='subtype',
            field=models.CharField(choices=[('Desk-with-cupboard', 'Desk with Cupboard'), ('Desk-without-cupboard', 'Desk without Cupboards'), ('2-Seater-Working-table', '2 Seater Working Table'), ('3-Seater-working-table', '3 Seater Working Table'), ('Chair-with-study-desk', 'Chair with Study Desk Attached'), ('Wooden-chair', 'Wooden Chair'), ('Steel-chair', 'Steel Chair'), ('Metal-Revolving-Chair', 'Metal Revolving Chair'), ('Conference-Table', 'Conference Table'), ('Whiteboard', 'Whiteboard'), ('Blackboard', 'Blackboard'), ('Pinboard', 'Pinboard'), ('Noticeboard', 'Noticeboard')], max_length=50),
        ),
    ]