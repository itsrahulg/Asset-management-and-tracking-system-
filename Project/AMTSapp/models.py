from django.db import models
import datetime

class Software(models.Model):
    LOCATIONS = [
        ('isl_lab', 'ISL Lab'),
        ('cc_lab', 'CC Lab'),
        ('project_lab', 'Project Lab'),
        ('ibm_lab', 'IBM Lab'),
        # ('g1_class_first_year', 'G1 Class First Year'),
        # ('g1_class_second_year', 'G1 Class Second Year'),
        # ('g2_class_first_year', 'G2 Class First Year'),
        ('K505_seminar_hall', 'K505-Seminar Hall'),
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
    

# class SoftwareUpdateLog(models.Model):
#     ASSET_ID = models.CharField(max_length=50)
#     brand = models.CharField(max_length=50)
#     model = models.CharField(max_length=50)
#     software_version = models.CharField(max_length=50)
#     date_of_purchase = models.DateField()
#     stock_register_number = models.CharField(max_length=50)
#     account_head = models.CharField(max_length=100)
#     location = models.CharField(max_length=50)
#     updated_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the update occurred
#     update_date = models.DateField()  # Field to manually enter the update date

#     def __str__(self):
#         return f"Update Log for {self.ASSET_ID} at {self.updated_at}"

#     # Method to display location in a more readable format
#     def get_location_display(self):
#         # Define a mapping of locations to friendly names
#         location_mapping = {
#             'isl_lab': 'ISL Lab',
#             'cc_lab': 'CC Lab',
#             'project_lab': 'Project Lab',
#             'ibm_lab': 'IBM Lab',
#             'g1_class_first_year': 'G1 Class First Year',
#             'g1_class_second_year': 'G1 Class Second Year',
#             'g2_class_first_year': 'G2 Class First Year',
#             'g2_class_second_year': 'G2 Class Second Year',
#             'wireless_communication_lab': 'Wireless Communication Laboratory',
#             'library': 'Library',
#         }
#         # Return the user-friendly name or the original value if not found
#         return location_mapping.get(self.location, self.location)


#updated update log model for the software assets
from django.contrib.auth.models import User

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
    updated_by = models.CharField(max_length=100, null=True)  # Manually entered field for who updated the software
    logged_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # User who logs the update

    def __str__(self):
        return f"Update Log for {self.ASSET_ID} at {self.updated_at}"

    def get_location_display(self):
        location_mapping = {
            'isl_lab': 'ISL Lab',
            'cc_lab': 'CC Lab',
            'project_lab': 'Project Lab',
            'ibm_lab': 'IBM Lab',
            # 'g1_class_first_year': 'G1 Class First Year',
            # 'g1_class_second_year': 'G1 Class Second Year',
            # 'g2_class_first_year': 'G2 Class First Year',
            'K505-Seminar Hall': 'K505-Seminar Hall',
            'wireless_communication_lab': 'Wireless Communication Laboratory',
            'library': 'Library',
        }
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
        # ('g1_class_first_year', 'G1 Class First Year'),
        # ('g1_class_second_year', 'G1 Class Second Year'),
        # ('g2_class_first_year', 'G2 Class First Year'),
        ('K505_seminar_hall', 'K505-Seminar-Hall'),
        ('wireless_communication_lab', 'Wireless Communication Laboratory'),
        ('e_learning_center', 'E-learning-Center'),
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


# #model to store the updated details of computer assets 
# from django.utils import timezone

# class ComputerHardwareUpdateLog(models.Model):
#     computer_hardware = models.ForeignKey(ComputerHardware, on_delete=models.CASCADE)
#     ASSET_ID = models.CharField(max_length=50)
#     brand = models.CharField(max_length=50, blank=True)
#     model = models.CharField(max_length=50, blank=True)
#     processor = models.CharField(max_length=50)
#     processor_generation = models.CharField(max_length=50)
#     ram = models.CharField(max_length=50)
#     rom = models.CharField(max_length=50, blank=True)
#     motherboard = models.CharField(max_length=50, blank=True)
#     power_supply = models.CharField(max_length=50, blank=True)
#     graphics_card = models.CharField(max_length=50, blank=True)
#     date_of_purchase = models.DateField()
#     stock_register_number = models.CharField(max_length=50)
#     account_head = models.CharField(max_length=100)
#     location = models.CharField(max_length=50)
#     date_logged = models.DateTimeField(auto_now_add=True)
#     date_of_update = models.DateField(default=timezone.now)  # New field with default date

#     def __str__(self):
#         # Format date_logged to show only the date
#         return f"Update Log: {self.ASSET_ID} - {self.date_logged.date()}"

#     def get_full_location(self):
#         # Map location abbreviations to full names
#         location_mapping = {
#             'isl_lab': 'ISL Lab',
#             'cc_lab': 'CC Lab',
#             'project_lab': 'Project Lab',
#             'ibm_lab': 'IBM Lab',
#             'g1_class_first_year': 'G1 Class First Year',
#             'g1_class_second_year': 'G1 Class Second Year',
#             'g2_class_first_year': 'G2 Class First Year',
#             'g2_class_second_year': 'G2 Class Second Year',
#             'wireless_communication_lab': 'Wireless Communication Laboratory',
#             'library': 'Library',
#         }
#         return location_mapping.get(self.location, self.location)

#modified update log model for computer hardware model
from django.contrib.auth.models import User
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
    date_of_update = models.DateField(default=timezone.now)
    updated_by = models.CharField(max_length=100, null=True)  # Field for who updated the hardware
    logged_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # User who logs the update

    def __str__(self):
        return f"Update Log: {self.ASSET_ID} - {self.date_logged.date()}"

    def get_full_location(self):
        location_mapping = {
            'isl_lab': 'ISL Lab',
            'cc_lab': 'CC Lab',
            'project_lab': 'Project Lab',
            'ibm_lab': 'IBM Lab',
            # 'g1_class_first_year': 'G1 Class First Year',
            # 'g1_class_second_year': 'G1 Class Second Year',
            # 'g2_class_first_year': 'G2 Class First Year',
            'K505_seminar_hall': 'K505-Seminar-Hall',
            'wireless_communication_lab': 'Wireless Communication Laboratory',
            'e_learning_center':'E-learning-Center',
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


#model to store the movement history of the computer hardware assets
class ComputerHardwareMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('within_college', 'Within the College'),
        ('outside', 'Outside the College')
    ]
    
    # Copy all fields from the ComputerHardware model
    ASSET_ID = models.CharField(max_length=50)
    hardware_type = models.CharField(max_length=50)
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

    # Additional movement-specific fields
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    new_location = models.CharField(max_length=255)
    reason = models.TextField()
    date_of_movement = models.DateField()
    date_logged = models.DateField(default=datetime.date.today)

    @classmethod
    def log_movement(cls, hardware, movement_type, new_location, reason, date_of_movement):
        return cls.objects.create(
            ASSET_ID=hardware.ASSET_ID,
            hardware_type=hardware.hardware_type,
            brand=hardware.brand,
            model=hardware.model,
            processor=hardware.processor,
            processor_generation=hardware.processor_generation,
            ram=hardware.ram,
            rom=hardware.rom,
            motherboard=hardware.motherboard,
            power_supply=hardware.power_supply,
            graphics_card=hardware.graphics_card,
            date_of_purchase=hardware.date_of_purchase,
            stock_register_number=hardware.stock_register_number,
            account_head=hardware.account_head,
            location=hardware.location,
            movement_type=movement_type,
            new_location=new_location,
            reason=reason,
            date_of_movement=date_of_movement,
            date_logged=datetime.date.today()
        )

    def __str__(self):
        return f"{self.ASSET_ID} moved {self.movement_type} to {self.new_location}"
    











#model for projector
from django.utils import timezone
class Projector(models.Model):
    LOCATIONS = [
        ('isl_lab', 'ISL Lab'),
        ('cc_lab', 'CC Lab'),
        ('project_lab', 'Project Lab'),
        ('ibm_lab', 'IBM Lab'),
        # ('g1_class_first_year', 'G1 Class First Year'),
        # ('g1_class_second_year', 'G1 Class Second Year'),
        # ('g2_class_first_year', 'G2 Class First Year'),
        ('K505_seminar_hall', 'K505-Seminar Hall'),
        ('e_learning_center', 'E-learning-Center'),
        ('wireless_communication_lab', 'Wireless Communication Laboratory'),
        # ('library', 'Library'),
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
# class ProjectorUpdateLog(models.Model):
#     projector = models.ForeignKey(Projector, on_delete=models.CASCADE)
#     updated_date = models.DateField(default=timezone.now)
#     brand = models.CharField(max_length=50)
#     model = models.CharField(max_length=50)
#     resolution = models.CharField(max_length=10)
#     lumens = models.IntegerField()
#     contrast_ratio = models.CharField(max_length=20)
#     connectivity = models.CharField(max_length=50)
#     lamp_life_hours = models.IntegerField()
#     date_of_purchase = models.DateField()
#     stock_register_number = models.CharField(max_length=50)
#     account_head = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)  # Full location name

#     def __str__(self):
#         return f"Update Log for {self.projector.ASSET_ID}"







#modified model to store the updated projector assets details
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
    updated_by = models.CharField(max_length=100,null=True)  # Field for who updated the record
    logged_by = models.CharField(max_length=100,null=True)  # Field to store the username of the logged-in user

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


#model for movement history of projector assets
class ProjectorMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('within_college', 'Within the College'),
        ('outside', 'Outside the College')
    ]

    ASSET_ID = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    resolution = models.CharField(max_length=10, choices=[
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
        ('4K', '4K')
    ])
    lumens = models.IntegerField(default=2000)
    contrast_ratio = models.CharField(max_length=20, blank=True)
    connectivity = models.CharField(max_length=50, null=True, blank=True)
    lamp_life_hours = models.IntegerField(default=2000)
    date_of_purchase = models.DateField(default=datetime.date.today)
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    
    # Movement fields
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    new_location = models.CharField(max_length=255)
    reason = models.TextField()
    date_of_movement = models.DateField()
    date_logged = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.ASSET_ID} moved {self.movement_type} to {self.new_location}"

    @classmethod
    def log_movement(cls, projector, movement_type, new_location, reason, date_of_movement):
        return cls.objects.create(
            ASSET_ID=projector.ASSET_ID,
            brand=projector.brand,
            model=projector.model,
            resolution=projector.resolution,
            lumens=projector.lumens,
            contrast_ratio=projector.contrast_ratio,
            connectivity=projector.connectivity,
            lamp_life_hours=projector.lamp_life_hours,
            date_of_purchase=projector.date_of_purchase,
            stock_register_number=projector.stock_register_number,
            account_head=projector.account_head,
            location=projector.location,
            movement_type=movement_type,
            new_location=new_location,
            reason=reason,
            date_of_movement=date_of_movement
        )




#model for books
class Books(models.Model):
    LOCATIONS = [
        ('isl_lab', 'ISL Lab'),
        ('cc_lab', 'CC Lab'),
        ('project_lab', 'Project Lab'),
        ('ibm_lab', 'IBM Lab'),
        # ('g1_class_first_year', 'G1 Class First Year'),
        # ('g1_class_second_year', 'G1 Class Second Year'),
        # ('g2_class_first_year', 'G2 Class First Year'),
        # ('g2_class_second_year', 'G2 Class Second Year'),
        ('wireless_communication_lab', 'Wireless Communication Laboratory'),
        # ('library', 'Library'),
        ('K505_seminar_hall', 'K505-Seminar Hall'),
        ('e_learning_center', 'E-learning-Center'),
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




# #model to update the books table and create an update log
# class BookUpdateLog(models.Model):
#     book = models.ForeignKey(Books, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     publisher = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     publishing_house = models.CharField(max_length=255)
#     edition = models.CharField(max_length=50, blank=True, null=True)
#     date_of_purchase = models.DateField()
#     stock_register_number = models.CharField(max_length=50)
#     account_head = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     date_logged = models.DateField(default=timezone.now)  # Update log timestamp
#     date_of_update = models.DateField()  # Manual entry for the update date

#     def __str__(self):
#         return f"Update log for {self.book.title} - {self.date_logged}"
    




#modified book update model to include the two additional fields
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
    date_logged = models.DateField(default=timezone.now)  # Log timestamp
    date_of_update = models.DateField()  # Manual entry for the update date
    updated_by = models.CharField(max_length=100,null=True)  # Text input for updated_by
    logged_by = models.CharField(max_length=100,null=True)  # Store the logged-in user's username

    def __str__(self):
        return f"Update log for {self.book.title} - {self.date_logged}"











#model for invalid book entry
class InvalidBookEntry(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishing_house = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    date_of_movement = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Invalid Entry: {self.ASSET_ID} - {self.title}"


#model to create table for scrapped books entry
class ScrappedBookAsset(models.Model):
    ASSET_ID = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishing_house = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    date_of_purchase = models.DateField()
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    date_of_movement = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Scrapped Entry: {self.ASSET_ID} - {self.title}"




#model to move the books to the movement history table
class MovedBooks(models.Model):
    MOVEMENT_CHOICES = [
        ('within_college', 'Within College'),
        ('outside_college', 'Outside College'),
    ]
    
    # Fields from the original Books model
    ASSET_ID = models.CharField(max_length=50, default='TEMP_ID')
    type_of_asset = models.CharField(max_length=50, default='Book')
    title = models.CharField(max_length=255,blank=True, null=True)
    publisher = models.CharField(max_length=255,blank=True, null=True)
    author = models.CharField(max_length=255,blank=True, null=True)
    publishing_house = models.CharField(max_length=255,blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True)
    date_of_purchase = models.DateField(default=datetime.date.today)  # Default to current date
    stock_register_number = models.CharField(max_length=50,blank=True, null=True)
    account_head = models.CharField(max_length=100,blank=True, null=True)
    original_location = models.CharField(max_length=50)
    
    # Movement-related fields
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    date_of_movement = models.DateField(default=datetime.date.today)
    new_location = models.CharField(max_length=255)  # Changed to text input
    reason_for_movement = models.TextField()

    def __str__(self):
        return f"Moved: {self.title} by {self.author} on {self.date_of_movement}"







#computer peripherals model
class ComputerPeripherals(models.Model):
    LOCATIONS = [
        ('isl_lab', 'ISL Lab'),
        ('cc_lab', 'CC Lab'),
        ('project_lab', 'Project Lab'),
        ('ibm_lab', 'IBM Lab'),
        ('wireless_communication_lab', 'Wireless Communication Laboratory'),
        ('K505_seminar_hall', 'K505-Seminar Hall'),
        ('e_learning_center', 'E-learning-Center'),
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



# #model to create computer peripheral update log
# class ComputerPeripheralsUpdateLog(models.Model):
#     peripheral = models.ForeignKey(ComputerPeripherals, on_delete=models.CASCADE)
#     peripheral_type = models.CharField(max_length=50)
#     brand = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     date_of_purchase = models.DateField()
#     stock_register_number = models.CharField(max_length=50)
#     account_head = models.CharField(max_length=100)
#     location = models.CharField(max_length=50)
#     date_logged = models.DateField(default=timezone.now)  # Log creation date
#     date_of_update = models.DateField()  # Manual update date entry

#     def __str__(self):
#         return f"Update log for {self.peripheral.peripheral_type} - {self.date_logged}"


#modified model for the computer peripheral update form
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
    updated_by = models.CharField(max_length=100,default="Lab Incharge")  # Text input for 'updated_by'
    logged_by = models.CharField(max_length=100,default="MCA")  # Username of the current logged-in user

    def __str__(self):
        return f"Update log for {self.peripheral.peripheral_type} - {self.date_logged}"











#model for invalid computer Peripheral assets
class InvalidComputerPeripherals(models.Model):
    # Fields from the original ComputerPeripherals model
    ASSET_ID = models.CharField(max_length=50)
    type_of_asset = models.CharField(max_length=50, default='Computer Peripheral')
    peripheral_type = models.CharField(max_length=50, choices=ComputerPeripherals.PERIPHERALS)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date_of_purchase = models.DateField(default=datetime.date.today)
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=ComputerPeripherals.LOCATIONS)
    
    # Additional fields for invalid peripherals
    date_of_movement = models.DateField(default=datetime.date.today)
    reason = models.TextField()
    date_logged = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Invalid {self.peripheral_type} - {self.ASSET_ID}"




#model for scrapped computer peripheral assets
class ScrappedComputerPeripherals(models.Model):
    # Fields from the original ComputerPeripherals model
    ASSET_ID = models.CharField(max_length=50)
    type_of_asset = models.CharField(max_length=50, default='Computer Peripheral')
    peripheral_type = models.CharField(max_length=50, choices=ComputerPeripherals.PERIPHERALS)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date_of_purchase = models.DateField(default=datetime.date.today)
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=ComputerPeripherals.LOCATIONS)

    # Additional fields for scrapped peripherals
    date_of_movement = models.DateField(default=datetime.date.today)
    reason = models.TextField()
    date_logged = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Scrapped {self.peripheral_type} - {self.ASSET_ID}"





#model for movement history for computer peripheral 
class MovedComputerPeripherals(models.Model):
    MOVEMENT_CHOICES = [
        ('within_college', 'Within College'),
        ('outside_college', 'Outside College'),
    ]

    # Fields from the original ComputerPeripherals model
    ASSET_ID = models.CharField(max_length=50)
    type_of_asset = models.CharField(max_length=50, default='Computer Peripheral')
    peripheral_type = models.CharField(max_length=50, choices=[
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
    ])
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date_of_purchase = models.DateField(default=datetime.date.today)
    stock_register_number = models.CharField(max_length=50)
    account_head = models.CharField(max_length=100)

    # Original location as a text field
    original_location = models.CharField(max_length=50)

    # Movement details
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    date_of_movement = models.DateField(default=datetime.date.today)
    new_location = models.CharField(max_length=255)  # Text input for new location
    reason_for_movement = models.TextField()

    # Log fields
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Moved {self.peripheral_type} ({self.ASSET_ID}) on {self.date_of_movement}"
















# class NetworkSwitch(models.Model):
#     asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
#     brand = models.CharField(max_length=50, blank=True)
#     model = models.CharField(max_length=50, blank=True)

#     def __str__(self):
#         return f"{self.asset.ASSET_ID} - Network Switch"


#furniture model to input furniture assets into the database
from django.db import models

from django.db import models

class Furniture(models.Model):
    ASSET_ID = models.CharField(max_length=50, primary_key=True)  # Manual entry for asset ID

    TYPE_OF_FURNITURE_CHOICES = [
        ('desk', 'Desk'),
        ('chair', 'Chair'),
        ('cupboard', 'Cupboard'),
        ('almirah', 'Almirah'),
        ('table', 'Table'),
        ('board', 'Board'),
    ]
    
    SUBTYPE_CHOICES = [
        ('desk_with_cupboard', 'Desk with Cupboard'),
        ('desk_without_cupboard', 'Desk without Cupboards'),
        ('2_seater_working_table', '2 Seater Working Table'),
        ('3_seater_working_table', '3 Seater Working Table'),
        ('chair_with_study_desk', 'Chair with Study Desk Attached'),
        ('wooden_chair', 'Wooden Chair'),
        ('steel_chair', 'Steel Chair'),
        ('metal_revolving_chair', 'Metal Revolving Chair'),
        ('conference_table', 'Conference Table'),
        ('whiteboard', 'Whiteboard'),
        ('blackboard', 'Blackboard'),
        ('pinboard', 'Pinboard'),
        ('noticeboard', 'Noticeboard'),
    ]

    LOCATION_CHOICES = [
        ('isl_lab', 'ISL Lab'),
        ('cc_lab', 'CC Lab'),
        ('project_lab', 'Project Lab'),
        ('ibm_lab', 'IBM Lab'),
        ('wireless_communication_lab', 'Wireless Communication Laboratory'),
        ('K505_seminar_hall', 'K505-Seminar Hall'),
        ('e_learning_center', 'E-learning Center'),
    ]
    
    type_of_furniture = models.CharField(max_length=50, choices=TYPE_OF_FURNITURE_CHOICES)
    subtype = models.CharField(max_length=50, choices=SUBTYPE_CHOICES)
    date_of_purchase = models.DateField()
    account_head = models.CharField(max_length=100)  # Adjust max_length as needed
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

    def __str__(self):
        return f"{self.type_of_furniture} - {self.subtype}"






    


