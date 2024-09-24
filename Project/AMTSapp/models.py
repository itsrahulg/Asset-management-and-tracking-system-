from django.db import models
import datetime

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

    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    date_of_purchase = models.DateField(default=datetime.date.today)  # Default to current date
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATIONS)
    type_of_asset = models.CharField(max_length=50, default='software')
    software_version = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.ASSET_ID} - {self.type_of_asset} - {self.brand} - {self.model}"
    

class SoftwareUpdateLog(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    software_version = models.CharField(max_length=50)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the update occurred
    update_date = models.DateField()  # Field to manually enter the update date

    def __str__(self):
        return f"Update Log for {self.ASSET_ID} at {self.updated_at}"

    # Method to display location in a more readable format
    def get_location_display(self):
        # Define a mapping of locations to friendly names
        location_mapping = {
            'isl_lab': 'ISL Lab',
            'cc_lab': 'CC Lab',
            'project_lab': 'Project Lab',
            'ibm_lab': 'IBM Lab',
            'g1_class_first_year': 'G1 Class First Year',
            'g1_class_second_year': 'G1 Class Second Year',
            'g2_class_first_year': 'G2 Class First Year',
            'g2_class_second_year': 'G2 Class Second Year',
            'wireless_communication_lab': 'Wireless Communication Laboratory',
            'library': 'Library',
        }
        # Return the user-friendly name or the original value if not found
        return location_mapping.get(self.location, self.location)




#models to store invalid entry and the scrapped assets details
class InvalidSoftwareEntry(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    type_of_asset = models.CharField(max_length=50)
    software_version = models.CharField(max_length=50, blank=True, null=True)
    date_of_movement = models.DateField()
    reason = models.TextField()
    date_logged = models.DateField(auto_now_add=True)


#model to store the scrapped assets
class ScrappedSoftwareAsset(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    type_of_asset = models.CharField(max_length=50)
    software_version = models.CharField(max_length=50, blank=True, null=True)
    date_of_movement = models.DateField()
    reason = models.TextField()
    date_logged = models.DateField(auto_now_add=True)



#model to store the movement history of software 
class SoftwareMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('within_college', 'Within the College'),
        ('outside', 'Outside the College')
    ]

    # Original software fields (logged for historical tracking)
    asset_id = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    software_version = models.CharField(max_length=50, blank=True, null=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    original_location = models.CharField(max_length=50)  # Previous location of software

    # Movement-specific fields
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    new_location = models.CharField(max_length=255)
    reason = models.TextField()
    date_of_movement = models.DateField()
    date_logged = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.asset_id} moved {self.movement_type} to {self.new_location}"
 




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
    
        ASSET_ID = models.CharField(max_length=50, default='CHW-XXX')
        hardware_type = models.CharField(max_length=50, default='Computer')
        brand = models.CharField(max_length=50, blank=True)
        model = models.CharField(max_length=50, blank=True)
        processor = models.CharField(max_length=50, choices=PROCESSOR_BRANDS)
        processor_generation = models.CharField(max_length=50, choices=PROCESSOR_GENERATIONS)
        ram = models.CharField(max_length=50, choices=RAM_CHOICES)
        rom = models.CharField(max_length=50, blank=True)
        motherboard = models.CharField(max_length=50, blank=True)
        power_supply = models.CharField(max_length=50, blank=True)
        graphics_card = models.CharField(max_length=50, blank=True)

        date_of_purchase = models.DateField(default=datetime.date.today)  # Default to current date
        stock_register_number = models.CharField(max_length=50)
        account_head = models.CharField(max_length=100)
        location = models.CharField(max_length=50, choices=LOCATIONS,)
        

        def __str__(self):
            return f"{self.asset.ASSET_ID} - Computer Hardware - {self.processor}"


#model to store the updated details of computer assets 
from django.utils import timezone

class ComputerHardwareUpdateLog(models.Model):
    computer_hardware = models.ForeignKey(ComputerHardware, on_delete=models.CASCADE)
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=50)
    processor_generation = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50, blank=True)
    motherboard = models.CharField(max_length=50, blank=True)
    power_supply = models.CharField(max_length=50, blank=True)
    graphics_card = models.CharField(max_length=50, blank=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    date_logged = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateField(default=timezone.now)  # New field with default date

    def __str__(self):
        # Format date_logged to show only the date
        return f"Update Log: {self.ASSET_ID} - {self.date_logged.date()}"

    def get_full_location(self):
        # Map location abbreviations to full names
        location_mapping = {
            'isl_lab': 'ISL Lab',
            'cc_lab': 'CC Lab',
            'project_lab': 'Project Lab',
            'ibm_lab': 'IBM Lab',
            'g1_class_first_year': 'G1 Class First Year',
            'g1_class_second_year': 'G1 Class Second Year',
            'g2_class_first_year': 'G2 Class First Year',
            'g2_class_second_year': 'G2 Class Second Year',
            'wireless_communication_lab': 'Wireless Communication Laboratory',
            'library': 'Library',
        }
        return location_mapping.get(self.location, self.location)



#model to store the invalid entry details for the computer hardware assets
class InvalidComputerHardwareEntry(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=50)
    processor_generation = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50, blank=True)
    motherboard = models.CharField(max_length=50, blank=True)
    power_supply = models.CharField(max_length=50, blank=True)
    graphics_card = models.CharField(max_length=50, blank=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_of_movement = models.DateField()
    reason = models.TextField()
    date_logged = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invalid Entry - {self.ASSET_ID}"




#model to store the scrapped computer hardware details
class ScrappedComputerHardwareAsset(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=50)
    processor_generation = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50, blank=True)
    motherboard = models.CharField(max_length=50, blank=True)
    power_supply = models.CharField(max_length=50, blank=True)
    graphics_card = models.CharField(max_length=50, blank=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_of_movement = models.DateField()
    reason = models.TextField()
    date_logged = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Scrapped Asset - {self.ASSET_ID}"




#model for projector
from django.utils import timezone
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

    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    resolution = models.CharField(max_length=10, choices=RESOLUTIONS)
    lumens = models.IntegerField(default=2000)
    contrast_ratio = models.CharField(max_length=20, blank=True)
    connectivity = models.CharField(max_length=50, choices=CONNECTIVITY_OPTIONS,null=True)
    lamp_life_hours = models.IntegerField(default=2000)
    date_of_purchase = models.DateField(default=datetime.date.today)  # Default to current date
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATIONS)
    type_of_asset = models.CharField(max_length=50,default='PROJECTOR')
    
    def __str__(self):
        return f"{self.ASSET_ID} - Projector - {self.brand} {self.model}"

    

#model to create an update log for the projector assets
class ProjectorUpdateLog(models.Model):
    projector = models.ForeignKey(Projector, on_delete=models.CASCADE)
    updated_date = models.DateField(default=timezone.now)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    resolution = models.CharField(max_length=10)
    lumens = models.IntegerField()
    contrast_ratio = models.CharField(max_length=20)
    connectivity = models.CharField(max_length=50)
    lamp_life_hours = models.IntegerField()
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # Full location name

    def __str__(self):
        return f"Update Log for {self.projector.ASSET_ID}"
    


#model for the invalid and scrapped projector assets
class InvalidProjectorEntry(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    resolution = models.CharField(max_length=10)
    lumens = models.IntegerField()
    contrast_ratio = models.CharField(max_length=20, blank=True)
    connectivity = models.CharField(max_length=50)
    lamp_life_hours = models.IntegerField()
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type_of_asset = models.CharField(max_length=50)
    date_of_movement = models.DateField()
    reason = models.TextField()
    date_logged = models.DateField(default=datetime.date.today)

class ScrappedProjectorAsset(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    resolution = models.CharField(max_length=10)
    lumens = models.IntegerField()
    contrast_ratio = models.CharField(max_length=20, blank=True)
    connectivity = models.CharField(max_length=50)
    lamp_life_hours = models.IntegerField()
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type_of_asset = models.CharField(max_length=50)
    date_of_movement = models.DateField()
    reason = models.TextField()
    date_logged = models.DateField(default=datetime.date.today)







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
    
    edition = models.CharField(max_length=50, blank=True, null=True)
    date_of_purchase = models.DateField(default=datetime.date.today)  # Default to current date
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATIONS)

    def __str__(self):
        return f"{self.ASSET_ID} - {self.title} by {self.author}"




#model to update the books table and create an update log
class BookUpdateLog(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishing_house = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_logged = models.DateField(default=timezone.now)  # Update log timestamp
    date_of_update = models.DateField()  # Manual entry for the update date

    def __str__(self):
        return f"Update log for {self.book.title} - {self.date_logged}"
    









    

#computer peripherals model
class ComputerPeripherals(models.Model):
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

    PERIPHERALS = [
        ('keyboard', 'Keyboard'),
        ('mouse', 'Mouse'),
        ('monitor', 'Monitor'),
        ('printer', 'Printer'),
        ('scanner', 'Scanner'),
        ('ups', 'UPS'),
        ('projector', 'Projector'),
        ('external_hard_drive', 'External Hard Drive'),
        ('router', 'Router'),
        ('switch', 'Switch'),
        ('webcam', 'Webcam'),
        ('hdmi_cable', 'HDMI Cable'),
        ('vga_cable', 'VGA Cable'),
        ('usb_cable', 'USB Cable'),
        ('ethernet_cable', 'Ethernet Cable'),
        ('power_cable', 'Power Cable'),
        ('adapter', 'Adapter'),
        # Add more peripherals as needed
    ]

    ASSET_ID = models.CharField(max_length=50)  # Placeholder removed
    type_of_asset = models.CharField(max_length=50, default='Computer Peripheral')
    peripheral_type = models.CharField(max_length=50, choices=PERIPHERALS)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date_of_purchase = models.DateField(default=datetime.date.today)  # Default to current date
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATIONS)

    def __str__(self):
        return f"{self.ASSET_ID} - {self.peripheral_type} ({self.brand} {self.model})"



#model to create computer peripheral update log
class ComputerPeripheralsUpdateLog(models.Model):
    peripheral = models.ForeignKey(ComputerPeripherals, on_delete=models.CASCADE)
    peripheral_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    date_logged = models.DateField(default=timezone.now)  # Log creation date
    date_of_update = models.DateField()  # Manual update date entry

    def __str__(self):
        return f"Update log for {self.peripheral.peripheral_type} - {self.date_logged}"






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






    


