from django.db import models

class Asset(models.Model):
    ASSET_TYPES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('computer_peripherals', 'Computer Peripherals'),
        ('furniture', 'Furniture'),
        ('book', 'Books'),
        ('miscellaneous', 'Miscellaneous'),
        ('other', 'Other'),
    ]

    HARDWARE_TYPE_CHOICES = [
        ('computer', 'Computer'),
        ('projector', 'Projector'),
        ('switch', 'Switch'),
        ('tubelight', 'Tubelight'),
        ('fan', 'Fan'),
        ('smartboard', 'Smartboard'),
        ('projector_screen', 'Projector Screen'),
    ]

    LOCATIONS = [
        ('isl_lab', 'ISL Lab'),
        ('cc_lab', 'CC Lab'),
        ('project_lab', 'Project Lab'),
        ('ibm_lab', 'IBM Lab'),
        ('g1_class_first_year', 'G1 Class First Year'),
        ('g1_class_second_year', 'G1 Class Second Year'),
        ('g2_class_first_year', 'G2 Class First Year'),
        ('g2_class_second_year', 'G2 Class Second Year'),
        ('wireless_communication_lab', 'Wireless Communication Laboratory'),
        ('library', 'Library'),
    ]

    ASSET_ID = models.CharField(max_length=50, default='TEMP_ID')
    type_of_asset = models.CharField(max_length=50, choices=ASSET_TYPES)
    specifications = models.TextField(blank=True)
    date_of_purchase = models.DateField()
    make_and_model = models.CharField(max_length=100, blank=True)
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATIONS)

    # Hardware specific fields
    hardware_type = models.CharField(max_length=50, choices=HARDWARE_TYPE_CHOICES, blank=True)
    processor = models.CharField(max_length=50, blank=True)
    ram = models.CharField(max_length=50, blank=True)
    rom = models.CharField(max_length=50, blank=True)
    motherboard = models.CharField(max_length=50, blank=True)
    power_supply = models.CharField(max_length=50, blank=True)
    graphics_card = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.ASSET_ID} - {self.type_of_asset} - {self.make_and_model}"
