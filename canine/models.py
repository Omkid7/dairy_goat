import random
from ast import Try
from datetime import date
from email.policy import default
from io import BytesIO, StringIO
from re import T
from statistics import mode
from tkinter import CASCADE
from unicodedata import category

import qrcode
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.cache import cache
from django.core.files import File
from django.core.validators import BaseValidator
from django.db import models
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.db.models.functions import Now
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from djgeojson.fields import PolygonField
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from PIL import Image, ImageDraw


class Location(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    dog_picture = models.ImageField()
    geom = PolygonField()

    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url
    
    @property
    def dog_picture_url(self):
        return self.dog_picture.url


class CustomUser(AbstractUser):
    user_type_data = ((1, "AdminHOD"), (2, "Pharmacist"), (3, "Doctor"), (4, "Clerk"),(5, "Handler"),(6, "Incharge"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Unit(models.Model):
    unit_name=models.CharField(max_length=30, null=True, blank=True)
    location=models.CharField(max_length=20, null=True, blank=True)
    address=models.CharField(max_length=30, null=True, blank=True)
        
    def __str__(self):
        return str(self.unit_name)
    

    
class Handler(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )        
    admin = models.OneToOneField(CustomUser,null=True, on_delete=models.CASCADE)
    reg_no=models.CharField(max_length=30,null=True,blank=True,unique=True)
    gender=models.CharField(max_length=7,null=True,blank=True,choices=gender_category)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateTimeField(auto_now_add= False, auto_now=False,null=True,blank=True)
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    profile_pic=models.ImageField(default="patient.jpg",null=True,blank=True)
    age= models.IntegerField(blank=True, null=True)
    address=models.CharField(max_length=10,null=True,blank=True)
    date_admitted=models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.admin)
    
class Incharge(models.Model):   
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )       
    admin = models.OneToOneField(CustomUser,null=True, on_delete=models.CASCADE)
    reg_no=models.CharField(max_length=30,null=True,blank=True,unique=True)
    gender=models.CharField(max_length=7,null=True,blank=True,choices=gender_category)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateTimeField(auto_now_add= False, auto_now=False,null=True,blank=True)
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    profile_pic=models.ImageField(default="patient.jpg",null=True,blank=True)
    age= models.IntegerField(blank=True, null=True)
    address=models.CharField(max_length=10,null=True,blank=True)
    date_admitted=models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.admin)
    
    
    
    
    
class Mwt(models.Model):
    team_leader = models.ForeignKey(Handler,null=True, on_delete=models.CASCADE)
    team_number = models.IntegerField( blank=True, null=True)
    team_specialization = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.team_leader)



class AdminHOD(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no= models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="admin.png",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_employed=models.DateTimeField(auto_now_add=True, auto_now=False)
    objects = models.Manager()
    def __str__(self):
        return str(self.admin)
    


class Pharmacist(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no=models.CharField(max_length=100,null=True,blank=True)
    age= models.IntegerField(blank=True, null=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile =models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="images2.png",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    
    def __str__(self):
        return str(self.admin)

 
 
# veterinary model   
class Doctor(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no=models.CharField(max_length=100,null=True,blank=True)
    age= models.IntegerField(blank=True, null=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="doctor.png",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.admin)
    
    
class Certification(models.Model):
    certification_number=models.IntegerField(null=True, blank=True)
    certification_date=models.DateField(auto_now_add=True, auto_now=False)
    details=models.TextField(blank=True,max_length=1000,null=True)
    authorized_by=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.certification_number)
	

class Clerk(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="images2.png",null=True,blank=True)
    age= models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.admin)
	
    

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    
    def __str__(self):
        return str(self.name)
	

    
# class Prescription(models.Model):
#     patient_id = models.ForeignKey(Dog,null=True, on_delete=models.SET_NULL)
#     description=models.TextField(null=True)
#     prescribe=models.CharField(max_length=100,null=True)
#     date_precribed=models.DateTimeField(auto_now_add=True, auto_now=False)
    
    
class Classification(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.name)



class ExpiredManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().annotate(
            
            
            expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
        )
        
class Owner(models.Model):
    name=models.CharField(max_length=30,blank=True, null=True,verbose_name='Name')
    address=models.CharField(max_length=45 ,blank=True, null=True,verbose_name='Address ')
    tele_phone=models.IntegerField(blank=True, null=True,verbose_name='Telephone Number')
    title=models.CharField(max_length=45 ,blank=True, null=True,verbose_name='Title')
    foreman=models.CharField(max_length=45 ,blank=True, null=True,verbose_name='Foreman')
    
    def __str__(self):
        return str(self.name)
    
def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
           ((today.month, today.day) < (born.month, born.day))

@deconstructible
class MaxAgeValidator(BaseValidator):
    message=("Age must not be more than %(limit_value)d.")
    code = 'max_age'

    def compare(self, a, b):
        return calculate_age(a) > b
    

# dog module 
class Dog(models.Model):   
    class_category=(
        ('Sniffing Dog', 'Sniffing Dog'),
        ('Sentries Dog', 'Sentries Dog'),
        ('Combative Dog', 'Combative Dog'),    
    )
    
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    dob=models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING,blank=True,verbose_name='Breed')
    dog_imprint=models.ForeignKey(Classification, max_length=45 ,blank=True,null=True,on_delete=models.DO_NOTHING,verbose_name='Classification')
    dog_name = models.CharField(max_length=50, blank=True, null=True,verbose_name='Dog Name')
    dog_color = models.CharField(max_length=50, blank=True, null=True,verbose_name='Colour')
    svc_age = models.IntegerField(blank=True, null=True,verbose_name='Service Age')
    svc_no = models.IntegerField(blank=True, null=True,verbose_name='Service Number', unique=True)
    reorder_level = models.IntegerField( blank=True, null=True,verbose_name='Kennel Number')
    manufacture= models.ForeignKey(Owner, on_delete=models.DO_NOTHING, blank=True, null=True,verbose_name='Owner')
    vetinary= models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, blank=True, null=True,verbose_name='Veterinary')
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    valid_from = models.DateField(blank=True, null=True,default=timezone.now)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    valid_to = models.DateField(blank=True, null=True)
    dog_description=models.TextField(blank=True,max_length=1000,null=True,verbose_name='Dog Description')
    dog_pic=models.ImageField(default="images2.png",null=True,blank=True,verbose_name='Canine Dog Image')
    emp_id = models.CharField(max_length=70, default=str(random.randrange(100,999,1)), verbose_name='Service Number')
    qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)
    objects = ExpiredManager()
   
    def __str__(self):
        return str(self.dog_name)
    
    # def get_absolute_url(self):
    #     return reverse('jobapp:applicant-details',  args=[str(self.pk)])  
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make({self.dog_name,self.category,self.emp_id})
        canvas = Image.new('RGB', [400, 380], 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        link_qr = f'qr_code-{self.dog_imprint,self.dog_name,self.emp_id,self.category}'+ '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(link_qr, File(buffer), save = False)
        canvas.close()
        super().save(*args, **kwargs)
    
    
    
class WeaponTraining(models.Model):
       
    ratings=(
        ('Satisfactory', 'Satisfactory'),
        ('Unsatisfactory', 'Unsatisfactory'),
   
    ) 
    weapon=models.CharField(max_length=30, null=True, blank=True, verbose_name="Utilization Training")
    dog=models.ForeignKey(Dog, max_length=30, null=True, blank=True, on_delete=models.DO_NOTHING)   
    building=models.CharField(max_length=30, null=True, blank=True, verbose_name='Building Search')
    gunfire_handler=models.CharField(max_length=30, null=True, blank=True, verbose_name='Gunfire Handler')
    gunfire_decoy=models.CharField(max_length=30, null=True, blank=True, verbose_name='Gunfire Decoy')
    tracking=models.CharField(max_length=30, null=True, blank=True, verbose_name='Tracking')
    daily_training_rating=models.CharField(max_length=30, null=True, blank=True, choices=ratings, verbose_name='Daily Training Rating')
    date=models.DateTimeField(blank=False, null=True)
    remarks=models.TextField(max_length=20,blank=True, null=True, verbose_name="Handlers Remarks")

    
    def __str__(self):
        return str(self.weapon)
    
    
class LeashTraining(models.Model):   
    ratings=(
        ('Satisfactory', 'Satisfactory'),
        ('Unsatisfactory', 'Unsatisfactory'),
   
    )  
    leash=models.CharField(max_length=30, null=True, blank=True, verbose_name="Leash Training")
    dog=models.ForeignKey(Dog, max_length=30, null=True, blank=True, on_delete=models.DO_NOTHING)
    onleash=models.CharField(max_length=30,null=True, blank=True,verbose_name='On leash Obedience')
    offleash=models.CharField(max_length=30,null=True, blank=True, verbose_name='Off leash Obedience')
    obedience_course=models.CharField(max_length=30,null=True, blank=True, verbose_name='Obedience Course')
    daily_training_rating=models.CharField(max_length=30, null=True, blank=True, choices=ratings, verbose_name='Daily Training Rating')
    date=models.DateTimeField(blank=False, null=True)
    remarks=models.TextField(max_length=20,blank=True, null=True, verbose_name="Handlers Remarks")


    
    def __str__(self):
        return str(self.leash)
    
class ControlledTraining(models.Model):   
    ratings=(
        ('Satisfactory', 'Satisfactory'),
        ('Unsatisfactory', 'Unsatisfactory'),
   
    )  
    controlled=models.CharField(max_length=30, null=True, blank=True, verbose_name="Controlled Training")
    dog=models.ForeignKey(Dog, max_length=30, null=True, blank=True, on_delete=models.DO_NOTHING)
    false_run=models.CharField(max_length=30, null=True, blank=True, verbose_name='False Run')
    attack=models.CharField(max_length=30, null=True, blank=True, verbose_name='Attack')
    search_and_attack=models.CharField(max_length=30, null=True, blank=True, verbose_name='Search and Attack')
    standoff=models.CharField(max_length=30, null=True, blank=True, verbose_name='Stand Off')
    effort=models.CharField(max_length=30, null=True, blank=True, verbose_name='Effort')
    daily_training_rating=models.CharField(max_length=30, null=True, blank=True, choices=ratings, verbose_name='Daily Training Rating')
    date=models.DateTimeField(blank=False, null=True)
    remarks=models.TextField(max_length=20,blank=True, null=True, verbose_name="Handlers Remarks")

    
    def __str__(self):
        return str(self.controlled)
    
class ScoutingTraining(models.Model):   
    ratings=(
        ('Satisfactory', 'Satisfactory'),
        ('Unsatisfactory', 'Unsatisfactory'),
   
    )  
    scounting=models.CharField(max_length=30, null=True, blank=True, verbose_name="Scounting Training")
    dog=models.ForeignKey(Dog, max_length=30, null=True, blank=True, on_delete=models.DO_NOTHING)
    scent_detection=models.CharField(max_length=30, blank=True, null=True, verbose_name='Scent Detection')
    sight_detection=models.CharField(max_length=30, blank=True, null=True, verbose_name='Sight Detection')
    sound_detection=models.CharField(max_length=30, blank=True, null=True, verbose_name='Sound Detection')
    vehicle_patrol=models.CharField(max_length=30, null=True, blank=True, verbose_name='Vehicle Patrol')
    daily_training_rating=models.CharField(max_length=30, null=True, blank=True, choices=ratings, verbose_name='Daily Training Rating')
    date=models.DateTimeField(blank=False, null=True)
    remarks=models.TextField(max_length=20,blank=True, null=True, verbose_name="Handlers Remarks")

    
    def __str__(self):
        return str(self.scounting)
    
    
    
class Utilization(models.Model):
    ratings=(
        ('Satisfactory', 'Satisfactory'),
        ('Unsatisfactory', 'Unsatisfactory'),     
    )
    utilization=models.CharField(max_length=30, null=True, blank=True, verbose_name="Utilization Training")
    dog=models.ForeignKey(Dog, on_delete=models.DO_NOTHING, max_length=30,verbose_name='Dog Name')
    combat_support=models.CharField(max_length=30, null=True, blank=True, verbose_name='Combat Support Operations')
    patrol_law_enforcement=models.CharField(max_length=30, null=True, blank=True, verbose_name='Patrol law Enforcement')
    patrol_security=models.CharField(max_length=30, blank=True, null=True, verbose_name='Patrol Security')
    daily_training_ratings=models.CharField(max_length=30, blank=True, null=True, choices=ratings, verbose_name='Daily Training Rating')
    date=models.DateTimeField(null=True, blank=True)
    remarks=models.TextField(max_length=20,blank=True, null=True, verbose_name="Handlers Remarks")

    
    def __str__(self):
        return str(self.utilization) 
    
class HandlerScores(models.Model):
    dog=models.ForeignKey(Dog, null=True, blank=True, on_delete=models.DO_NOTHING, max_length=30,verbose_name='Dog Name')
    weapon=models.ForeignKey(WeaponTraining, null=True, blank=True, on_delete=models.DO_NOTHING, max_length=30,verbose_name='Weapon Training')
    leash=models.ForeignKey(LeashTraining, null=True, blank=True, on_delete=models.DO_NOTHING, max_length=30,verbose_name='Leash Training')
    controlled=models.ForeignKey(ControlledTraining, null=True, blank=True, on_delete=models.DO_NOTHING, max_length=30,verbose_name='Controlled Training')
    scounting=models.ForeignKey(ScoutingTraining, null=True, blank=True, on_delete=models.DO_NOTHING, max_length=30,verbose_name='Scounting Training')
    utilization=models.ForeignKey(Utilization, null=True, blank=True, on_delete=models.DO_NOTHING, max_length=30,verbose_name='Dog Name')
    remarks=models.TextField(max_length=20,blank=True, null=True, verbose_name="Handlers Remarks")

    
    def __str__(self):
        return str(self.dog) 
    
     

class Course(models.Model):
    course_code=models.IntegerField( null=True, blank=True, verbose_name='Course Code')
    course_name=models.CharField(max_length=30, blank=True, null=True, verbose_name='Course Name')
    location=models.CharField(max_length=30, null=True, blank=True, verbose_name='Location')
    course_start_date=models.DateField(auto_now=True, blank=False)
    course_completion=models.DateField(auto_now=True, blank=True)
    
    def __str__(self):
        return str(self.course_name)
    
    
class Training(models.Model):
    dog=models.ForeignKey(Dog,null=True, on_delete=models.SET_NULL, verbose_name='Name of The Dog')
    chip_number=models.IntegerField( blank=True, null=True)
    course=models.ForeignKey(Course,null=True, on_delete=models.SET_NULL, verbose_name='Course Name')
    trainer=models.ForeignKey(Handler,null=True, on_delete=models.SET_NULL, verbose_name='Trainers Name')
    passed_out_no=models.IntegerField( null=True, blank=True)
    authorized=models.ForeignKey(Doctor,null=True, on_delete=models.SET_NULL, verbose_name='Authorized by')
    
    def __str__(self):
        return str(self.chip_number)
    
    
class Training_day_session(models.Model):
    status_category=(
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    date=models.DateField(auto_now_add=True)
    handler=models.ForeignKey(Handler, on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=30, null=True, blank=True)
    num_of_activities=models.IntegerField(blank=True, null=True)
    num_of_hours=models.IntegerField(null=True, blank=True)
    dog=models.ForeignKey(Dog, on_delete=models.DO_NOTHING, max_length=30)
    status=models.CharField(max_length=30, null=True, choices=status_category)
    
    def __str__(self):
        return str(self.handler)
    
class MonthlyBody(models.Model):
    dog_id=models.ForeignKey(Dog, null=True, on_delete=models.SET_NULL,verbose_name='Canine Dog' )
    date=models.DateField(null=True, blank=True)
    weight=models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
       return str(self.dog_id)
   
   
class Deworming(models.Model):
    name=models.CharField(max_length=30, null=True, blank=True, verbose_name="Name of Deworming")
    
    def __str__(self):
       return str(self.name)


class Type_of_deworming(models.Model):
    dog=models.ForeignKey(Dog, null=True, on_delete=models.DO_NOTHING,verbose_name='Canine Dog' )
    name=models.ForeignKey(Deworming, null=True, on_delete=models.DO_NOTHING,verbose_name='Type of Deworming' )
    valid_from = models.DateField(blank=True, null=True,default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    product=models.CharField(max_length=30, null=True, blank=True, verbose_name="Product Name")
    amount=models.IntegerField(null=True, blank=True, verbose_name="Amount")
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    valid_to = models.DateField(blank=False, null=True)
    objects = ExpiredManager()


    def __str__(self):
       return str(self.dog)
   
class VaccinationCategory(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True, verbose_name='Type of Vaccination')
    
    def __str__(self):
       return str(self.name)
   
class VaccinationType(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True, verbose_name='Type of Vaccination')
    
    def __str__(self):
       return str(self.name)
   
class Vaccination(models.Model):
    category=models.ForeignKey(VaccinationCategory, null=True, blank=True, on_delete=models.DO_NOTHING,verbose_name='Vaccine Category' )
    name=models.CharField(null=True, blank=True, max_length=30, verbose_name="Vaccine Name")
    manufacture=models.CharField(null=True, blank=True, max_length=30, verbose_name="Manufacturer")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    valid_from = models.DateField(blank=True, null=True,default=timezone.now)
    valid_to = models.DateField(blank=True, null=True)
    receive_quantity = models.IntegerField( blank=True, null=True)
    reorder_level = models.IntegerField( blank=True, null=True)
    quantity = models.IntegerField( blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    drug_pic=models.ImageField(default="images2.png",null=True,blank=True,verbose_name='Drug Image')
    quantity = models.IntegerField( blank=True, null=True,verbose_name='Quantity')
    batch_no = models.CharField(max_length=30, blank=True, null=True,verbose_name='Vaccine Batch Number')
    reorder_level = models.IntegerField( blank=True, null=True,verbose_name='Add Reorder Level Number')
    objects = ExpiredManager()

     
    def __str__(self):
       return str(self.name)
   

    
class Assessment(models.Model):
    acceptance_category=(
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    )
    accessor=models.CharField(max_length=50,null=True, verbose_name='Assessor') 
    date_of_assessment=models.DateField(auto_now=True, verbose_name='Assessment Date')
    dog=models.ForeignKey(Dog, null=True, on_delete=models.SET_NULL,verbose_name='Canine Dog' )
    discipline_criteria=models.CharField(max_length=50, blank=True, null=True,verbose_name='Discipline Cretiria')
    requirements=models.CharField(max_length=50, blank=True, null=True,verbose_name='Requirements')
    comment=models.TextField(null=True, blank=True, verbose_name='Comment')
    acceptance=models.CharField(max_length=50, blank=True, null=True, choices=acceptance_category, verbose_name='Acceptance')
   
    def __str__(self):
        return str(self.accessor)
    
    
class SkillTest(models.Model):
    
    test_category=(
        ('Sniffing Test', 'Sniffing Test'),
        ('Sentries Test', 'Sentries Test')
    )
    
    competent_category=(
        ('Good', 'Good'),
        ('Very Good', 'Very Good'),
        ('Outstanding', 'Outstanding')
    )
    dog=models.ForeignKey(Dog, null=True, on_delete=models.SET_NULL,verbose_name='Canine Dog' )
    test_type=models.CharField(max_length=50, blank=True, null=True, choices=test_category, verbose_name='Acceptance')
    criteria_detail=models.CharField(max_length=50, blank=True, null=True, verbose_name='Criteria Details')
    competent=models.CharField(max_length=50, blank=True, null=True, choices=competent_category, verbose_name='Acceptance')
    comments=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.dog)
    
    
class Casting(models.Model):
    dog=models.ForeignKey(Dog, max_length=30, on_delete=models.DO_NOTHING)
    training_evaluation=models.CharField(max_length=30, null=True, blank=True)
    veterinary_evaluation=models.CharField(max_length=30, null=True, blank=True)
    vaccination=models.CharField(max_length=30, null=True, blank=True)
    history=models.TextField(null=True, blank=True)
    veterinary_reccomendation=models.CharField(max_length=30, null=True, blank=True)
    casting_reason=models.TextField(null=True, blank=True)
    casting_authority=models.ForeignKey(Doctor, max_length=30, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return str(self.casting_reason)
    
    
class Employment(models.Model):
    deployment=(
        ('Within the Country', 'Within the Country'),
        ('Outside the Country', 'Outside the Country')
    )
    status_category=(
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    dog=models.ForeignKey(Dog, max_length=30, null=True, blank=True, on_delete=models.DO_NOTHING)
    type_of_deployment=models.CharField(max_length=30, null=True, blank=True, choices=deployment)
    team=models.ForeignKey(Mwt, max_length=30, on_delete=models.DO_NOTHING)
    description=models.TextField(null=True, blank=True)
    date_of_start=models.DateField(auto_now_add=True, auto_now=False)
    status=models.CharField(max_length=30, null=True, blank=True, choices=status_category)
    
    def __str__(self):
        return str(self.type_of_deployment)
    
    
class Inventory(models.Model):
    inventory_type=(
        ('Expandable', 'Expandable'),
        ('Consumable', 'Consumable')
    )
    
    status=(
        ('Serviceable', 'Serviceable'),
        ('Unserviceable', 'Unserviceable')
    )
    tracking_number=models.IntegerField( null=False, blank=False)
    inventory=models.CharField(max_length=30, choices=inventory_type)
    data_received=models.DateField(auto_now_add=True)
    serviceability_status=models.CharField(max_length=30, choices=status)
    assigned_to=models.ForeignKey(Handler, max_length=20,on_delete=models.DO_NOTHING)
    notes=models.TextField(null=False, blank=True)
    
    def __str__(self):
        return str(self.tracking_number)
    
    
    
        
    
class Prescription(models.Model):
    

    status_category=(
        ('Normal', 'Normal'),
        ('Abnormal', 'Abnormal')
    ) 
    
    dog_id=models.ForeignKey(Dog,null=True, on_delete=models.SET_NULL, verbose_name='Name of The Dog')
    vaccination_id=models.ForeignKey(Vaccination ,max_length=50, blank=True, on_delete=models.SET_NULL, null=True,verbose_name='Type of Vaccine')
    description=models.TextField(null=True, verbose_name='Condition of the Dog')
    prescribe=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=50, blank=True, null=True,verbose_name='Status', choices=status_category)
    veterinary_id=models.ForeignKey(Doctor,  on_delete=models.CASCADE, blank=True, null=True,verbose_name='Doctor' )
    vac_batch_no=models.IntegerField(null=True, blank=True, verbose_name='Vaccination Batch Number')
    vet_remarks=models.TextField(max_length=100, null=True, blank=True, verbose_name="Veterinary Remarks")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    valid_from = models.DateField(blank=True, null=True,default=timezone.now)
    valid_to = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    objects = ExpiredManager() 
    
    def __str__(self):
        return str(self.dog_id)
    

   
    
class Dispense(models.Model):  
    handler_id = models.ForeignKey(Handler, on_delete=models.DO_NOTHING,null=True)
    dog_id = models.ForeignKey(Dog, on_delete=models.SET_NULL,null=True,blank=False,verbose_name='Canine Dog')
    dispense_svc_age = models.PositiveIntegerField(default='1', blank=False, null=True, verbose_name='Age')
    taken=models.CharField(max_length=300,null=True, blank=True)
    dog_ref_no=models.CharField(max_length=300,null=True, blank=True)
    instructions=models.TextField(max_length=300,null=True, blank=False)
    dispense_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)


class HandlerFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    handler_id = models.ForeignKey(Handler, on_delete=models.CASCADE)
    admin_id= models.ForeignKey( AdminHOD,null=True, on_delete=models.CASCADE)
    pharmacist_id=models.ForeignKey( Pharmacist,null=True, on_delete=models.CASCADE)
    feedback = models.TextField(null=True)
    feedback_reply = models.TextField(null=True)
    admin_created_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()





@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Pharmacist.objects.create(admin=instance,address="")
        if instance.user_type == 3:
            Doctor.objects.create(admin=instance,address="")
        if instance.user_type == 4:
            Clerk.objects.create(admin=instance,address="")
        if instance.user_type == 5:
            Handler.objects.create(admin=instance,address="")
        if instance.user_type == 6:
            Incharge.objects.create(admin=instance,address="")
       
       
       

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.pharmacist.save()
    if instance.user_type == 3:
        instance.doctor.save()
    if instance.user_type == 4:
        instance.clerk.save()
    if instance.user_type == 5:
        instance.handler.save()
    if instance.user_type == 6:
        instance.incharge.save()


   






 