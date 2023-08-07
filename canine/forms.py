from email.policy import default
from pyexpat import model
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import Form
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from leaflet.forms.widgets import LeafletWidget
import json



class HandlerPicForm1(forms.ModelForm):
    class Meta:
        model=Handler
        fields='__all__'
        exclude=['admin','gender','mobile','address','dob']
      


class DateInput(forms.DateInput):
    input_type = "date"

from phonenumber_field.formfields import PhoneNumberField

class ClientForm(forms.Form):
    mobile = PhoneNumberField()

class HandlerForm(forms.Form):

    username = forms.CharField(label='Surname',max_length=50, widget=forms.TextInput(attrs={"placeholder":"Username" ,"class":"form-control" }))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={"placeholder":"email", "class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    reg_no = forms.CharField(label='Service Number', max_length=50,widget=forms.TextInput(attrs={"placeholder":"Service Number", "class":"form-control"}))
    
    rank_list=(
       ('Choose Rank', 'Choose Rank'), 
       ('Pte', 'Pte'),
       ('Spte', 'Spte'),
       ('Cpl', 'Cpl'),
       ('Sgt', 'Sgt'),
       ('Ssgt', 'Ssgt'),
       ('W02', 'W02'), 
    )
    
    service_list=(
        ('Select Service', 'Select Service'), 
        ('Kenya Army', 'Kenya Army'),
        ('Kenya Airforce', 'Kenya Airforce'),
        ('Kenya Navy', 'Kenya Navy'),  
    )
    
    unit=(
        ('Choose Unit', 'Choose Unit'), 
        ('Canine BN', 'Canine BN'),
        ('Deftec', 'Deftec'),
        ('Cismic', 'Cismic'), 
        
    )
    
    first_name = forms.ChoiceField(
    label="Rank", initial="Choose Rank", choices=rank_list, widget=forms.Select(attrs={"class":"form-control"}))
    last_name = forms.ChoiceField(label="Service",choices=service_list, widget=forms.Select(attrs={"class":"form-control"}))
    address = forms.ChoiceField(label="Unit", initial="Choose Rank", choices=unit, widget=forms.Select(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Mobile", max_length=50,widget=forms.TextInput(attrs={"placeholder":"Mobile Number", "class":"form-control"}))
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    

    gender = forms.ChoiceField(label="Gender", initial="Choose Service", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    dob= forms.DateField(label="Registration Date", widget=DateInput(attrs={"class":"form-control"}))

    # Validations for Handler
    def clean_reg_no(self):
        reg_no = self.cleaned_data['reg_no']
        if  not  reg_no:
            raise ValidationError("This field is required")
        for instance in Handler.objects.all():
            if instance.reg_no==reg_no:
                raise ValidationError( "Service number aready exist")
      
        return reg_no


    def clean_phone_number(self):
        phone_number=self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError('This field is requied')
        elif len(phone_number) < 10:
            raise forms.ValidationError('Invalid Number')
        for instance in Handler.objects.all():
            if instance.phone_number==phone_number:
                raise ValidationError( "PhoneNumber aready exist")
        
        return phone_number
        
            
   
    def clean_username(self):
        username = self.cleaned_data['username']
        if  not  username:
            raise ValidationError("This field is required")
        for instance in CustomUser.objects.all():
            if instance.username==username:
                raise ValidationError( "Surname aready exist")
      
        return username

    def clean_firstName(self):
        first_name = self.cleaned_data['first_name']
        if  not  first_name:
            raise ValidationError("This field is required")
        return first_name

    def clean_secondName(self):
        last_name = self.cleaned_data['last_name']
        if  not  last_name:
            raise ValidationError("This field is required")
        return last_name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('password', css_class='form-group col-md-4 mb-0'),

                css_class='form-row'
            ),
         
            Row(
                Column('reg_no', css_class='form-group col-md-4 mb-0'),
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('username', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('address', css_class='form-group col-md-4 mb-0'),
                Column('phone_number', css_class='form-group col-md-4 mb-0'),
                Column('dob', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
             Row(
                Column('gender', css_class='form-group col-md-4 mb-0'),
             
                css_class='form-row'
            ),
            # 'check_me_out',
             Submit('submit', 'Submit')
        )

class EditHandlerForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    first_name = forms.CharField(label="Rank", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Service", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Unit", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Mobile", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    dob= forms.DateField(label="DOE", widget=DateInput(attrs={"class":"form-control"}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('password', css_class='form-group col-md-4 mb-0'),

                css_class='form-row'
            ),
         
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('username', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('phone_number', css_class='form-group col-md-4 mb-0'),
                Column('dob', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
             Row(
                Column('gender', css_class='form-group col-md-4 mb-0'),
             
                css_class='form-row'
            ),
            # 'check_me_out',
             Submit('submit', 'Submit')
   
        )
    

class DogForm(forms.ModelForm):
    # category = forms.CharField(label="Breed", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # dog_imprint = forms.CharField(label="Classification", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # dog_name = forms.CharField(label="Dog Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # dog_color = forms.CharField(label="Dog Colour", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # svc_age = forms.CharField(label="Service Age", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # manufacture = forms.CharField(label="Owner", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # dog_description = forms.CharField(label="Dog Description", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # dog_pic = forms.ImageField(label="Dog Image", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # gender_list = (
    #     ('Male','Male'),
    #     ('Female','Female')
    # )
    # gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    # dob= forms.DateField(label="Date of Birth", widget=DateInput(attrs={"class":"form-control"}))
  
    valid_to= forms.DateField(label="ROD", widget=DateInput(attrs={"class":"form-control"}))
    dob= forms.DateField(label="Date of Birth", widget=DateInput(attrs={"class":"form-control"}))


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('category', css_class='form-group col-md-4 mb-0'),
    #             Column('dog_imprint', css_class='form-group col-md-4 mb-0'),
    #             Column('dog_name', css_class='form-group col-md-4 mb-0'),

    #             css_class='form-row'
    #         ),
         
    #         Row(
    #             Column('dog_color', css_class='form-group col-md-4 mb-0'),
    #             Column('svc_age', css_class='form-group col-md-4 mb-0'),
    #             Column('manufacture', css_class='form-group col-md-4 mb-0'),

    #             css_class='form-row'
    #         ),
            
    #         Row(
    #             Column('gender', css_class='form-group col-md-4 mb-0'),
    #             Column('dob', css_class='form-group col-md-4 mb-0'),
    #             Column('valid_to', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
    #          Row(
    #             Column('dog_pic', css_class='form-group col-md-4 mb-0'),
             
    #             css_class='form-row'
    #         ),
    #         # 'check_me_out',
    #          Submit('submit', 'Submit')
   
    #     )
    class Meta:
        model=Dog
        fields='__all__'
        exclude=['valid_from', 'vetinary', 'qrcode', 'emp_id', 'reorder_level']

        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
      
        
class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields='__all__'
        widgets={'geom': LeafletWidget()}
   
        
class VaccinationTypeForm(forms.ModelForm):
    class Meta:
        model=VaccinationCategory
        fields='__all__'
        
class OwnerForm(forms.ModelForm):
    class Meta:
        model=Owner
        fields='__all__'
        
class UnitForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields='__all__'
        
        
class CertificationForm(forms.ModelForm):
    class Meta:
        model=Certification
        fields='__all__'
        
class Training_sessionForm(forms.ModelForm):
    class Meta:
        model=Training_day_session
        fields='__all__'
        
class MwtForm(forms.ModelForm):
    class Meta:
        model=Mwt
        fields='__all__'
        
class TrainingForm(forms.ModelForm):
    class Meta:
        model=Training
        fields='__all__'
        
class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
        
class ClassificationForm(forms.ModelForm):
    class Meta:
        model=Classification
        fields='__all__'
        
class AssessmentForm(forms.ModelForm):
    class Meta:
        model=Assessment
        fields='__all__'
        
class SkilltestForm(forms.ModelForm):
    class Meta:
        model=SkillTest
        fields='__all__'
        
class CastingForm(forms.ModelForm):
    class Meta:
        model=Casting
        fields='__all__'
        
class EmploymentForm(forms.ModelForm):
    class Meta:
        model=Employment
        fields='__all__'
        
class WeaponTrainingForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=WeaponTraining
        fields='__all__'
        exclude=['weapon']
        
class LeashTrainingForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=LeashTraining
        fields='__all__'
        exclude=['leash']
        
class ControlledTrainingForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=ControlledTraining
        fields='__all__'
        exclude=['controlled']
        
class ScountingTrainingForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=ScoutingTraining
        fields='__all__'
        exclude=['scounting']
        
class EditTrainingForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=WeaponTraining
        fields='__all__'       

class UtilizationForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Utilization
        fields='__all__'
        exclude=['utilization']

class PrescriptionForm(forms.ModelForm):
    valid_to= forms.DateField(label="Valid Until", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Prescription
        fields='__all__' 
        exclude=['veterinary_id', 'valid_from', ]
        

        
# class HandlerForm(forms.ModelForm):
#     class Meta:
#         model=HandlerScores
#         fields=['remarks'] 
        
class MonthlyBodyForm(forms.ModelForm):
    class Meta:
        model=MonthlyBody
        fields='__all__' 
        
class DewormingForm(forms.ModelForm):
    class Meta:
        model=Deworming
        fields='__all__'
        
class Type_of_DewormingForm(forms.ModelForm):
    valid_to= forms.DateField(label="Valid to", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Type_of_deworming
        fields='__all__'
        exclude=['valid_from']
        

        
class vaccinationForm(forms.ModelForm):
    valid_to= forms.DateField(label="Expiry Date", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Vaccination
        fields='__all__'  
        exclude=['valid_from','reorder_level','receive_svc_age']
        
class EditvaccinationForm(forms.ModelForm):
    valid_to= forms.DateField(label="Expiry Date", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Vaccination
        fields='__all__'  
        exclude=['valid_from','reorder_level','receive_svc_age']
        
class LeashRemarksForm(forms.ModelForm):
    class Meta:
        model=LeashTraining
        fields=['remarks'] 
        
class HandlerScoresForm(forms.ModelForm):
    class Meta:
        model=HandlerScores
        fields='__all__' 
        exclude=['remarks'] 
        
class MonthlyForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))
    class Meta:
        model=MonthlyBody
        fields='__all__' 
        
class EditMonthlyForm(forms.ModelForm):
    date= forms.DateField(label="Day of the Month", widget=DateInput(attrs={"class":"form-control"}))
    class Meta:
        model=MonthlyBody
        fields='__all__' 
        

class CustomerForm(ModelForm):
    class Meta:
        model=Pharmacist
        fields='__all__'
        exclude=['admin','gender','mobile','address']


       

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'
        exclude=['admin','gender','mobile','address']

        def clean_firstName(self):
            first_name = self.cleaned_data['first_name']
            if  not  first_name:
                raise ValidationError("This field is required")
            return first_name

        def clean_mobile(self):
            mobile=self.cleaned_data.get('mobile')
            if not mobile:
                raise forms.ValidationError('This field is requied')
            return mobile
        def clean_username(self):
            username = self.cleaned_data['username']
            if  not  username:
                raise ValidationError("This field is required")
            for instance in CustomUser.objects.all():
                if instance.username==username:
                    raise ValidationError( "Username aready exist")

class ClerkForm(ModelForm):
    class Meta:
        model=Clerk
        fields='__all__'
        exclude=['admin','gender','mobile','address']
        
class HodForm(ModelForm):
    class Meta:
        model=AdminHOD
        fields='__all__'
        exclude=['admin','gender','mobile','address']

class HandlerSearchForm1(ModelForm):
    
    class Meta:
        model=Handler
        fields='__all__'
        exclude=['profile_pic','gender','mobile','address','dob']
        
class HandlerForm7(ModelForm):
     class Meta:
        model=Handler
        fields='__all__'


class DispenseForm(ModelForm):
    # gender_list = (
       
    # )
    # dog_id = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
   
    class Meta:
        model=Dispense
        fields='__all__'
        exclude=['Dog_ref_no']
        
    #     dog_id = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # # def updateItem(self,request):
 
    #     data=json.loads(request.body)
    #     dogId=data['dogId']
    #     print('ACTION:',dogId)
    #     dog_name = forms.CharField(label="Mobile", max_length=50, widget=forms.TextInput(attrs={"value":dogId}))

    # # # Dog=Dog.objects.get(id=dogId)
    # # # # dogs=Dog.objects.all()
    # # # form=DispenseForm(request.POST or None,instance=Dog,initial={'Handler_id':queryset} )
    # # # if form.is_valid():
    # # #     instance=form.save(commit=False)
    # # #     instance.svc_age-=instance.dispense_svc_age
        
    # #     # instance.save()
    #     return JsonResponse('jamara dd',  safe=False)
 
class ReceiveDogForm(ModelForm):
    valid_to= forms.DateField(label="Expiry Date", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Dog
        fields='__all__'
        exclude=['category' ,'dog_name','valid_from','dispense_svc_age','reorder_level','date_from','date_to','svc_age','manufacture']


class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Dog
		fields = ['reorder_level']

