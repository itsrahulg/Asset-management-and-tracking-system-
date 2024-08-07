from django.db import models

class Software(models.Model):
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
    brand = models.CharField(max_length=50, blank=True, default='Unknown Brand')
    model = models.CharField(max_length=50, blank=True, default='Unknown Model')
    date_of_purchase = models.DateField(default='2000-01-01')  # Default to a date in the past
    stock_register_number = models.CharField(max_length=50, default='0000')
    account_head = models.CharField(max_length=100, default='Default Account Head')
    location = models.CharField(max_length=50, choices=LOCATIONS, default='isl_lab')
    
    type_of_asset = models.CharField(max_length=50, default='software')
    software_version = models.CharField(max_length=50, blank=True, null=True, default='1.0')

    def __str__(self):
        return f"{self.ASSET_ID} - {self.type_of_asset} - {self.brand} - {self.model}"
    






#computer model 

class ComputerHardware(models.Model):
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

        RAM_CHOICES = [
        ('2GB', '2GB'),
        ('4GB', '4GB'),
        ('8GB', '8GB'),
        ('12GB', '12GB'),
        ('16GB', '16GB'),
        ('32GB', '32GB'),
        ('64GB', '64GB'),
        ('128GB', '128GB'),
    ]
    
        PROCESSOR_BRANDS = [
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
    ]
    
        PROCESSOR_GENERATIONS = [
        ('1st Gen', '1st Gen'),
        ('2nd Gen', '2nd Gen'),
        ('3rd Gen', '3rd Gen'),
        ('4th Gen', '4th Gen'),
        ('5th Gen', '5th Gen'),
        ('6th Gen', '6th Gen'),
        ('7th Gen', '7th Gen'),
        ('8th Gen', '8th Gen'),
        ('9th Gen', '9th Gen'),
        ('10th Gen', '10th Gen'),
        ('11th Gen', '11th Gen'),
        ('12th Gen', '12th Gen'),
        ('13th Gen', '13th Gen'),
        ('14th Gen', '14th Gen'),
        ('15th Gen', '15th Gen'),
    ]
    
        ASSET_ID = models.CharField(max_length=50, default='TEMP_ID')
        hardware_type = models.CharField(max_length=50, default='computer')
        brand = models.CharField(max_length=50, blank=True)
        model = models.CharField(max_length=50, blank=True)
        processor = models.CharField(max_length=50, choices=PROCESSOR_BRANDS)
        processor_generation = models.CharField(max_length=50, choices=PROCESSOR_GENERATIONS)
        ram = models.CharField(max_length=50, choices=RAM_CHOICES)
        rom = models.CharField(max_length=50, blank=True)
        motherboard = models.CharField(max_length=50, blank=True)
        power_supply = models.CharField(max_length=50, blank=True)
        graphics_card = models.CharField(max_length=50, blank=True)

        date_of_purchase = models.DateField(default='2000-01-01')  # Default to a date in the past
        stock_register_number = models.CharField(max_length=50, default='0000')
        account_head = models.CharField(max_length=100, default='Default Account Head')
        location = models.CharField(max_length=50, choices=LOCATIONS, default='isl_lab')
        

        def __str__(self):
            return f"{self.asset.ASSET_ID} - Computer Hardware - {self.processor}"





#model for projector
class Projector(models.Model):
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
    
    RESOLUTIONS = [
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
        ('4K', '4K'),
    ]
    
    CONNECTIVITY_OPTIONS = [
        ('HDMI', 'HDMI'),
        ('VGA', 'VGA'),
        ('DVI', 'DVI'),
        ('USB', 'USB'),
        ('Wireless', 'Wireless'),
    ]

    ASSET_ID = models.CharField(max_length=50, default='TEMP_ID')
    brand = models.CharField(max_length=50, blank=True, default='Brand')
    model = models.CharField(max_length=50, blank=True, default='Model')
    resolution = models.CharField(max_length=10, choices=RESOLUTIONS, default='1080p')
    lumens = models.IntegerField(default=2000)
    contrast_ratio = models.CharField(max_length=20, blank=True, default='1000:1')
    connectivity = models.CharField(max_length=50, choices=CONNECTIVITY_OPTIONS, default='HDMI')
    lamp_life_hours = models.IntegerField(default=2000)
    date_of_purchase = models.DateField(default='2000-01-01')  # Default to a date in the past
    stock_register_number = models.CharField(max_length=50, default='0000')
    account_head = models.CharField(max_length=100, default='Default Account Head')
    location = models.CharField(max_length=50, choices=LOCATIONS, default='isl_lab')
    type_of_asset = models.CharField(max_length=50, default='hardware')
    
    def __str__(self):
        return f"{self.ASSET_ID} - Projector - {self.brand} {self.model}"

    





#model for books
class Books(models.Model):
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
    type_of_asset = models.CharField(max_length=50, default='Book')

    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishing_house = models.CharField(max_length=255)
    
    edition = models.CharField(max_length=50, blank=True, null=True, default='1.0')
    date_of_purchase = models.DateField(default='2000-01-01')
    stock_register_number = models.CharField(max_length=50, default='0000')
    account_head = models.CharField(max_length=100, default='Default Account Head')
    location = models.CharField(max_length=50, choices=LOCATIONS, default='isl_lab')

    def __str__(self):
        return f"{self.ASSET_ID} - {self.title} by {self.author}"










# class Fan(models.Model):
#     asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
#     brand = models.CharField(max_length=50, blank=True)
#     model = models.CharField(max_length=50, blank=True)

#     def __str__(self):
#         return f"{self.asset.ASSET_ID} - Fan"

# class Tubelight(models.Model):
#     asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
#     brand = models.CharField(max_length=50, blank=True)
#     model = models.CharField(max_length=50, blank=True)

#     def __str__(self):
#         return f"{self.asset.ASSET_ID} - Tubelight"

# class NetworkSwitch(models.Model):
#     asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
#     brand = models.CharField(max_length=50, blank=True)
#     model = models.CharField(max_length=50, blank=True)

#     def __str__(self):
#         return f"{self.asset.ASSET_ID} - Network Switch"



# class Furniture(models.Model):
#     FURNITURE_TYPES = [
#         ('Chair', 'Chair'),
#         ('Steel Chair', 'Steel Chair'),
#         ('Wooden Chair', 'Wooden Chair'),
#         ('Cabinet', 'Cabinet'),
#         ('Table', 'Table'),
#         ('Desk', 'Desk'),
#     ]

#     asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
#     furniture_type = models.CharField(max_length=50, choices=FURNITURE_TYPES)

#     def __str__(self):
#         return f"{self.asset.ASSET_ID} - Furniture - {self.furniture_type}"

# class Books(models.Model):
#     PUBLISHING_HOUSES = [
#         ('Penguin Random House', 'Penguin Random House'),
#         ('HarperCollins', 'HarperCollins'),
#         ('Simon & Schuster', 'Simon & Schuster'),
#         ('Hachette Livre', 'Hachette Livre'),
#         ('Macmillan Publishers', 'Macmillan Publishers'),
#         ('Scholastic', 'Scholastic'),
#     ]

#     asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
#     author = models.CharField(max_length=100, blank=True)
#     publisher = models.CharField(max_length=100, choices=PUBLISHING_HOUSES)

#     def __str__(self):
#         return f"{self.asset.ASSET_ID} - Books - {self.author}"




    

# class ComputerPeripherals(models.Model):
#     asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
#     brand = models.CharField(max_length=50, blank=True)
#     model = models.CharField(max_length=50, blank=True)

#     def __str__(self):
#         return f"{self.asset.ASSET_ID} - Computer Peripherals"
