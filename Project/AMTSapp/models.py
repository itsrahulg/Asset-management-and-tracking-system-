# models.py
from django.db import models

class Asset(models.Model):
    ASSET_TYPES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('furniture', 'Furniture'),
        ('other', 'Other'),
    ]

    LOCATIONS = [
        ('isl_lab', 'ISL Lab'),
        ('cc_lab', 'CC Lab'),
        ('project_lab', 'Project Lab'),
        ('ibm_lab', 'IBM Lab'),
        ('g1_class', 'G1 Class'),
        ('g2_class', 'G2 Class'),
    ]

    type_of_asset = models.CharField(max_length=50, choices=ASSET_TYPES)
    specifications = models.TextField()
    date_of_purchase = models.DateField()
    make_and_model = models.CharField(max_length=100)
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATIONS)

    def __str__(self):
        return f"{self.type_of_asset} - {self.make_and_model}"
