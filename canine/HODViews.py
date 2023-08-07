from unicodedata import name
from canine.clerkViews import receptionistProfile
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone, dateformat
from django.core.exceptions import ValidationError
from datetime import datetime
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import datetime 


from .forms import *
from .models import *

def map(request):
    return render(request, 'hod_templates/map.html')


def adminDashboard(request):
    handlers=Handler.objects.all().count()
    # categories=Dog.objects.filter(name='category').count()
    doctors=Doctor.objects.all().count()
    pharmacist=Pharmacist.objects.all().count() 
    receptionist=Clerk.objects.all().count() 
    prescip = Prescription.objects.all().count()

    out_of_dog=Dog.objects.filter(svc_age__lte=0).count()
    total_dog=Dog.objects.all().count()
    
    today = datetime.today()
    
    for_today = Handler.objects.filter(date_admitted__year=today.year, date_admitted__month=today.month, date_admitted__day=today.day).count()
    print(for_today)
    
    exipred=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True).count()
    
    
    distemper=Vaccination.objects.filter(category__name__icontains='Distemper').count()
    distemper=int(distemper)
    print("Number of distemper is", distemper)
    
    hepatitis=Vaccination.objects.filter(category__name__icontains='Hepatitis').count()
    hepatitis=int(hepatitis)
    print("Number of hepatitis is", hepatitis)
    
    leptasirosis=Vaccination.objects.filter(category__name__icontains='Leptospirosis').count()
    leptasirosis=int(leptasirosis)
    print("Number of labrador is", leptasirosis)
    
    parvovirus=Vaccination.objects.filter(category__name__icontains='Parvovirus').count()
    parvovirus=int(parvovirus)
    print("Number of parvovirus is", parvovirus)
    
    rabies=Vaccination.objects.filter(category__name__icontains='Rabies').count()
    rabies=int(rabies)
    print("Number of rabies is", rabies)
    
    vaccine_list=['Distemper', 'Hepatitis', 'Leptospirosis','Parvovirus', 'Rabies']
    num_vac=[distemper, hepatitis, leptasirosis, parvovirus, rabies]
    
       
    leash=LeashTraining.objects.all().count()
    leash=int(leash)
    print("leash is", leash)
    
    scounting=ScoutingTraining.objects.all().count()
    scounting=int(scounting)
    print("Scounting Number is", scounting)
    
    controlled=ControlledTraining.objects.all().count()
    controlled=int(controlled)
    print("controlled Number", controlled)
    
    utilization=Utilization.objects.all().count()
    utilization=int(utilization)
    print("utilization Number", utilization)
    
   
    bulldog=Dog.objects.filter(category__name__contains='bulldog').count()
    bulldog=int(bulldog)
    print("Number of bulldog is", bulldog)
    
    rotteler=Dog.objects.filter(category__name__contains='wrotteler').count()
    rotteler=int(rotteler)
    print("Number of rotteler is", rotteler)
    
    labrador=Dog.objects.filter(category__name__contains='Labrador Retriever').count()
    labrador=int(labrador)
    print("Number of labrador is", labrador)
    
    german=Dog.objects.filter(category__name__contains='German Shepherd').count()
    german=int(german)
    print("Number of german is", german)
    
    boxer=Dog.objects.filter(category__name__contains='Boxer').count()
    boxer=int(boxer)
    print("Number of Boxer is", boxer)
    
  
    
    explosive=Dog.objects.filter(dog_imprint__name__contains='Explosive').count()
    explosive=int(explosive)
    print("Number of bulldog is", explosive)
    
    protection=Dog.objects.filter(dog_imprint__name__contains='Protection Dog').count()
    protection=int(protection)
    print("Number of rotteler is", protection)
    
    infantry=Dog.objects.filter(dog_imprint__name__contains='Infantry Patrol Dogs').count()
    infantry=int(infantry)
    print("Number of labrador is", infantry)
    
    patrol=Dog.objects.filter(dog_imprint__name__contains='Patrol and Search Dogs').count()
    patrol=int(patrol)
    print("Number of patrol is", patrol)
    
    narcotic=Dog.objects.filter(dog_imprint__name__contains='Narcotic Dogs').count()
    narcotic=int(narcotic)
    print("Number of narcotic is", narcotic)
    
    explosive_search=Dog.objects.filter(dog_imprint__name__contains='Explosive Search Dogs').count()
    explosive_search=int(explosive_search)
    print("Number of labrador is", explosive_search)
    
    human=Dog.objects.filter(dog_imprint__name__contains='Human Detection Dogs(U/T').count()
    human=int(human)
    print("Number of labrador is", human)
    
    dog_weight=MonthlyBody.objects.filter(weight__lte='50').count()
    dog_weight=range(dog_weight)
    print("The Weight is", dog_weight)
    
  
    
    train_list=['Scounting', 'Controlled', 'Utilization', 'Leashing']
    train_num=[scounting,controlled,utilization,leash]
    
    breed_list=['bulldog', 'Boxer', 'Labrador Retriever','Wrotteler', 'German Shepherd']
    num_list=[bulldog, boxer, rotteler, labrador, german]
    
    class_list=['Explosive', 'Protection Dog', 'Infantry Patrol Dogs','Explosive Search Dogs', 'Human Detection Dogs(U/T)', 'Narcotic Dogs', 'Patrol and Search Dogs' ]
    class_num_list=[explosive, protection, infantry, explosive_search, human, narcotic, patrol ]
   
    weight_list=('Ben','Wiko', 'Dan', 'Allan')
    weight_num=(dog_weight)
   
    
    context={
        "handler_total":handlers,
        "expired_total":exipred,
        "out_of_dog":out_of_dog,
        "total_dogs":total_dog,
        "all_doctors":doctors,
        "all_pharmacists":pharmacist,
        "all_clerks":receptionist,
        "for_today":for_today,
        "prescip":prescip,
        "breed_list":breed_list,
        "num_list": num_list,
        "train_list":train_list,
        "train_num":train_num,
        "class_list":class_list,
        "class_num_list": class_num_list,
        "dog_weight": dog_weight,
        "weight_list": weight_list,
        "weight_num":weight_num,
        "vaccine_list": vaccine_list,
        "num_vac": num_vac
        
        
        # "category":category,

    }
    return render(request,'hod_templates/admin_dashboard.html',context)



def createhandler(request):
    form=HandlerForm()

 
    if request.method == "POST":
        form=HandlerForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            reg_no = form.cleaned_data['reg_no']



            user = CustomUser.objects.create_user(username=username, email=email,password=password, last_name=last_name,user_type=5)
            user.handler.address = address
            user.handler.phone_number = phone_number
            user.handler.dob=dob
            user.handler.reg_no=reg_no
            user.handler.first_name=first_name
            user.handler.last_name=last_name
            user.handler.gender=gender

            user.save()
            messages.success(request, username +' was Successfully Added')

            return redirect('all_handler')

          
   

    context={
        "form":form,
        "title":"Add Handler"
    }
       
    return render(request,'hod_templates/handler_form.html',context)



def allhandler(request):
    form=HandlerSearchForm1(request.POST or None)
    handler=Handler.objects.all()
    context={
        "handler":handler,
        "form":form,
        "title":"Registered Handlers"
    }
    if request.method == 'POST':
        # admin=form['first_name'].value()
        name = request.POST.get('search')
        handler=Handler.objects.filter(first_name__icontains=name) 
       
        context={
            "handler":handler,
            form:form
        }
    return render(request,'hod_templates/added_handler.html',context)

def confirmDelete(request,pk):
    try:
        handler=Handler.objects.get(id=pk)
        if request.method == 'POST':
            handler.delete()
            return redirect('all_handler')
    except:
        messages.error(request, "Handlers Cannot be deleted, Handlers is still on medication or an error occured")
        return redirect('all_handler')

    context={
        "handler":handler,

    }
    
    return render(request,'hod_templates/sure_delete.html',context)

   
@login_required
def createPharmacist(request):

    if request.method == "POST":
           
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
           
        
        user = CustomUser.objects.create_user(username=username, email=email,password=password, first_name=first_name, last_name=last_name,user_type=2)
        user.first_name=first_name
        user.last_name=last_name
        user.pharmacist.address = address
        user.pharmacist.mobile = mobile

        user.save()
        messages.success(request, "Staff Added Successfully!")
        return redirect('add_pharmacist')
       

    context={
    "title":"Add Trainer"

    }
    
    return render(request,'hod_templates/pharmacist_form.html',context)

def managePharmacist(request):
    staffs = Pharmacist.objects.all()
    context = {
        "staffs": staffs,
        "title":"Manage Veterinary"
    }

    return render(request,'hod_templates/all_pharmacist.html',context)

def createDoctor(request):

    if request.method == "POST":
           
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
           
        try:
            user = CustomUser.objects.create_user(username=username, email=email,password=password, first_name=first_name, last_name=last_name,user_type=3)
            user.doctor.address = address
            user.doctor.mobile = mobile

            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('manage_doctor')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_doctor')

    context = {
        "title":"Add Veterinary"

    }
    

    return render(request,'hod_templates/add_doctor.html',context)

def manageDoctor(request):
    staffs = Doctor.objects.all()

    context = {
        "staffs": staffs,
        "title":"Veterinary Details"

    }

    return render(request,'hod_templates/manage_doctor.html',context)

def createPharmacyClerk(request):

    if request.method == "POST":
           
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
           
        try:
            user = CustomUser.objects.create_user(username=username, email=email,password=password, first_name=first_name, last_name=last_name, user_type=4)
            user.clerk.address = address
            user.clerk.mobile = mobile


            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('manage_Clerk')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_Clerk')

    context = {
    "title":"Add Clerk"

}
    

    return render(request,'hod_templates/add_Clerk.html',context)

def managePharmacyClerk(request):
   

    staffs = Clerk.objects.all()
    context = {
        "staffs": staffs,
         "title":"Manage Clerk"
    }

    return render(request,'hod_templates/manage_Clerk.html',context)


def addDog(request):
    form=DogForm(request.POST,request.FILES)
    if form.is_valid():
        form=DogForm(request.POST,request.FILES)

        form.save()
        return redirect('manage_dog')
    
    context={
        "form":form,
        "title":"Add New Dog"
    }
    return render(request,'hod_templates/add_dog.html',context)


    
def manageDog(request):
    dogs = Dog.objects.all().order_by("-id")
    ex=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True)
    eo=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=False)
    

    context = {
        "dogs": dogs,
        "expired":ex,
        "expa":eo,
        "title":"Manage Available Dogs"
    }

    return render(request,'hod_templates/manage_dog.html',context)


def addCategory(request):
    try:
        form=CategoryForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Breed added Successfully!")

                return redirect('add_category')
    except:
        messages.error(request, "Breed Not added! Try again")

        return redirect('add_category')

    
    context={
        "form":form,
        "title":"Add a New Breed"
    }
    return render(request,'hod_templates/add_category.html',context)


def addCertification(request):
    try:
        form=CertificationForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Certificate added Successfully!")

                return redirect('add_certificate')
    except:
        messages.error(request, "Certificate Not added! Try again")

        return redirect('add_certificate')

    
    context={
        "form":form,
        "title":"Add Certificate"
    }
    return render(request,'hod_templates/add_category.html',context)


def addMwt(request):
    try:
        form=MwtForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Team added Successfully!")

                return redirect('add_team')
    except:
        messages.error(request, "Team Not added! Try again")

        return redirect('add_team')

    
    context={
        "form":form,
        "title":"Add a New Team"
    }
    return render(request,'hod_templates/add_team.html',context)


def addUnit(request):
    try:
        form=UnitForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Unit added Successfully!")

                return redirect('add_unit')
    except:
        messages.error(request, "Unit Not added! Try again")

        return redirect('add_unit')

    
    context={
        "form":form,
        "title":"Add a New Unit"
    }
    return render(request,'hod_templates/add_unit.html',context)

def addAssessment(request):
    try:
        form=AssessmentForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Assessment added Successfully!")

                return redirect('add_assessment')
    except:
        messages.error(request, "Assessment Not added! Try again")

        return redirect('add_assessment')

    
    context={
        "form":form,
        "title":"Add Assessment"
    }
    return render(request,'hod_templates/add_assessment.html',context)

def addSkilltest(request):
    try:
        form=SkilltestForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Skilltest added Successfully!")

                return redirect('add_skilltest')
    except:
        messages.error(request, "Skilltest Not added! Try again")

        return redirect('add_skilltest')

    
    context={
        "form":form,
        "title":"Add Skilltest"
    }
    return render(request,'hod_templates/add_skilltest.html',context)

def addOwner(request):
    try:
        form=OwnerForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Owner added Successfully!")

                return redirect('add_owner')
    except:
        messages.error(request, "Owner Not added! Try again")

        return redirect('add_owner')

    
    context={
        "form":form,
        "title":"Add The Owner"
    }
    return render(request,'hod_templates/add_owner.html',context)


def addTraining_sessions(request):
    try:
        form=Training_sessionForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Training Session added Successfully!")

                return redirect('add_training_session')
    except:
        messages.error(request, "Training Session Not added! Try again")

        return redirect('add_training_session')

    
    context={
        "form":form,
        "title":"Add Training Session"
    }
    return render(request,'hod_templates/add_training_session.html',context)

def addCasting(request):
    try:
        form=CastingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Casting added Successfully!")

                return redirect('add_casting')
    except:
        messages.error(request, "Casting Not added! Try again")

        return redirect('add_casting')

    
    context={
        "form":form,
        "title":"Casting"
    }
    return render(request,'hod_templates/add_casting.html',context)

def Employment(request):
    try:
        form=EmploymentForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Employment added Successfully!")

                return redirect('add_employment')
    except:
        messages.error(request, "Employment Not added! Try again")

        return redirect('add_employment')

    
    context={
        "form":form,
        "title":"Employment"
    }
    return render(request,'hod_templates/add_employment.html',context)


def addPrescription(request):
    form=PrescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prescribe')
    
    context={
        "form":form,
        "title":"Vaccine"
    }
    return render(request,'hod_templates/prescribe.html',context)

def addCourse(request):
    form=CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_course')
    
    context={
        "form":form,
        "title":"Courses"
    }
    return render(request,'hod_templates/add_course.html',context)


def addTraining(request):
    form=TrainingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('training')
    
    context={
        "form":form,
        "title":"Training"
    }
    return render(request,'hod_templates/training.html',context)



    
def edithandler(request,handler_id):
    # adds handler id into session variable
    request.session['handler_id'] = handler_id

    handler = Handler.objects.get(admin=handler_id)

    form = EditHandlerForm()
    

    # filling the form with data from the database
    form.fields['email'].initial = handler.admin.email
    form.fields['username'].initial = handler.admin.username
    form.fields['first_name'].initial = handler.first_name
    form.fields['last_name'].initial = handler.last_name
    form.fields['address'].initial = handler.address
    form.fields['gender'].initial = handler.gender
    form.fields['phone_number'].initial = handler.phone_number
    form.fields['dob'].initial = handler.dob
    if request.method == "POST":
        if handler_id == None:
            return redirect('all_handler')
        form = EditHandlerForm( request.POST)

        if form.is_valid():
            
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            dob=form.cleaned_data['dob']
            phone_number = form.cleaned_data['phone_number']


            try:
            # First Update into Custom User Model
                user = CustomUser.objects.get(id=handler_id)
                user.username = username

                user.email = email
                user.save()

                # Then Update Students Table
                handlers_edit = Handler.objects.get(admin=handler_id)
                handlers_edit.address = address
                handlers_edit.gender = gender
                handlers_edit.dob=dob
                handlers_edit.phone_number=phone_number
                handlers_edit.first_name = first_name
                handlers_edit.last_name = last_name


                
                handlers_edit.save()
                messages.success(request, "Handler Updated Successfully!")
                return redirect('all_handler')
            except:
                messages.success(request, "Failed to Update Handler.")
                return redirect('all_handler')


    context = {
        "id": handler_id,
        # "username": handler.admin.username,
        "form": form,
        "title":"Edit Handler"
    }
    return render(request, "hod_templates/edit_handler.html", context)


       

    
def handler_personalRecords(request,pk):
    handler=Handler.objects.get(id=pk)
    # prescrip=handler.prescription_set.all()
    dogs=handler.dispense_set.all()

    context={
        "handler":handler,
        # "prescription":prescrip,
        "dogs":dogs

    }
    return render(request,'hod_templates/handler_personalRecords.html',context)

def deletePrescription(request,pk):
    prescribe=Prescription.objects.get(id=pk)
    if request.method == 'POST':
        prescribe.delete()
        return redirect('all_handler')

    context={
        "handler":prescribe
    }

    return render(request,'hod_templates/sure_delete.html',context)


def hodProfile(request):
    customuser=CustomUser.objects.get(id=request.user.id)
    staff=AdminHOD.objects.get(admin=customuser.id)


    form=HodForm()
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
       
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')

        customuser=CustomUser.objects.get(id=request.user.id)
        customuser.first_name=first_name
        customuser.last_name=last_name
        customuser.save()

        staff=AdminHOD.objects.get(admin=customuser.id)
        form =HodForm(request.POST,request.FILES,instance=staff)
        staff.address = address
       
        staff.mobile=mobile
        staff.save()

        if form.is_valid():
            form.save()

    context={
        "form":form,
        "staff":staff,
        "user":customuser
    }

    return render(request,'hod_templates/hod_profile.html',context)

def deleteDoctor(request,pk):
    try:
        doctor=Doctor.objects.get(id=pk)
        if request.method == 'POST':
            doctor.delete()
            messages.success(request, "Veterinary  deleted successfully")

            return redirect('manage_doctor')

    except:
        messages.error(request, "Veterinary aready deleted")
        return redirect('manage_doctor')


   
    return render(request,'hod_templates/sure_delete.html')
    
def deletePharmacist(request,pk):
    try:
        pharmacist=Pharmacist.objects.get(id=pk)
        if request.method == 'POST':
            pharmacist.delete()
            messages.success(request, "Veterinary  deleted successfully")
                
            return redirect('manage_pharmacist')

    except:
        messages.error(request, "Veterinary aready deleted")
        return redirect('manage_pharmacist')


   
    return render(request,'hod_templates/sure_delete.html')

def deletePharmacyClerk(request,pk):
    try:
        clerk=Clerk.objects.get(id=pk)
        if request.method == 'POST':
        
       
            clerk.delete()
            messages.success(request, "Clerk  deleted   successfully")
                
            return redirect('manage_Clerk')

    except:
        messages.error(request, "Clerk Not deleted")
        return redirect('manage_Clerk')


   
    return render(request,'hod_templates/sure_delete.html')

def editPharmacist(request,staff_id):
    staff = Pharmacist.objects.get(admin=staff_id)
    if request.method == "POST":
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

            # INSERTING into Customuser Model
        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()
        
        # INSERTING into Staff Model
        staff = Pharmacist.objects.get(admin=staff_id)
        staff.address = address
        staff.save()

        messages.success(request, "Staff Updated Successfully.")
        return redirect('manage_pharmacist')
    context = {
        "staff": staff,
        "id": staff_id,
        'title':"Edit Trainer "

    }
    return render(request, "hod_templates/edit_pharmacist.html", context)


def editDoctor(request,doctor_id):
    staff = Doctor.objects.get(admin=doctor_id)
    if request.method == "POST":
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

            # INSERTING into Customuser Model
        user = CustomUser.objects.get(id=doctor_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()
        
        # INSERTING into Staff Model
        staff = Doctor.objects.get(admin=doctor_id)
        staff.address = address
        staff.save()

        messages.success(request, "Staff Updated Successfully.")

    context = {
        "staff": staff,
        "title":"Edit Veterinary"
    }
    return render(request, "hod_templates/edit_doctor.html", context)

def editPharmacyClerk(request,clerk_id):
    clerk=Clerk.objects.get(admin=clerk_id)
    if request.method == "POST":
        username = request.POST.get('username')
        last_name=request.POST.get('last_name')
        first_name=request.POST.get('first_name')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
    
        try:
            user=CustomUser.objects.get(id=clerk_id)
            user.email=email
            user.username=username
            user.first_name=first_name
            user.last_name=last_name
            user.save()

            clerk =Clerk.objects.get(admin=clerk_id)
            clerk.address=address
            clerk.mobile=mobile
            clerk.gender=gender
            clerk.save()

            messages.success(request,'Clerk Updated Succefully')
        except:
            messages.success(request,'An Error Was Encounterd Clerk Not Updated')


        
    context={
        "staff":clerk,
        "title":"Edit Clerk"


    }
    return render(request,'hod_templates/edit_clerk.html',context)


def editAdmin(request):
    customuser=CustomUser.objects.get(id=request.user.id)
    staff=AdminHOD.objects.get(admin=customuser.id)


    form=HodForm()
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
       
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')

        customuser=CustomUser.objects.get(id=request.user.id)
        customuser.first_name=first_name
        customuser.last_name=last_name
        customuser.save()

        staff=AdminHOD.objects.get(admin=customuser.id)
        form =HodForm(request.POST,request.FILES,instance=staff)
        staff.address = address
       
        staff.mobile=mobile
        staff.save()

        if form.is_valid():
            form.save()

    context={
        "form":form,
        "staff":staff,
        "user":customuser
    }

    return render(request,'hod_templates/edit-profile.html',context)


def editdog(request,pk):
    dogs=Dog.objects.get(id=pk)
    form=DogForm(request.POST or None,instance=dogs)

    if request.method == "POST":
        if form.is_valid():
            form=DogForm(request.POST or None ,instance=dogs)

            category=request.POST.get('category')
            dog_name=request.POST.get('dog_name')
            svc_age=request.POST.get('svc_age')
            # email=request.POST.get('email')

            try:
                dogs =Dog.objects.get(id=pk)
                dogs.dog_name=dog_name
                dogs.svc_age=svc_age
                dogs.save()
                form.save()
                messages.success(request,'Dog Updated Succefully')
            except:
                messages.error(request,'An Error Was Encounterd Dog Not Updated')


        
    context={
        "dogs":dogs,
         "form":form,
         "title":"Edit Dog"

    }
    return render(request,'hod_templates/edit_dog.html',context)


def deletedog(request,pk):
    try:
    
        dog=Dog.objects.get(id=pk)
        if request.method == 'POST':
        
            dog.delete()
            messages.success(request, "Veterinary  deleted successfully")
                
            return redirect('manage_dog')

    except:
        messages.error(request, "Veterinary aready deleted")
        return redirect('manage_dog')



    return render(request,'hod_templates/sure_delete.html')

def receivedog(request,pk):
    receive=Dog.objects.get(id=pk)
    form=ReceiveDogForm()
    try:
        form=ReceiveDogForm(request.POST or None )

        if form.is_valid():
            form=ReceiveDogForm(request.POST or None ,instance=receive)

            instance=form.save(commit=False) 
            instance.svc_age+=instance.receive_svc_age
            instance.save()
            form=ReceiveDogForm()

            messages.success(request, str(instance.receive_svc_age) + " " + instance.dog_name +" "+ "Dogs added successfully")

            return redirect('manage_dog')

      
    except:
        messages.error(request,"An Error occured, Dog  Not added")
                
        return redirect('manage_dog')
    context={
            "form":form,
            "title":"Add Dog"
            
        }
    return render(request,'hod_templates/modal_form.html',context)


def reorder_level(request, pk):
    queryset = Dog.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for " + str(instance.dog_name) + " is updated to " + str(instance.reorder_level))

        return redirect("manage_dog")
    context ={
        "instance": queryset,
        "form": form,
        "title":"Kennel Number"
    }

    return render(request,'hod_templates/reorder_level.html',context)

def dogDetails(request,pk):
    dogs=Dog.objects.get(id=pk)
    # prescrip=Dogs.prescription_set.all()
    # dogs=dogs.dispense_set.all()

    context={
        "dogs":dogs,
        # "prescription":prescrip,
        # "dogs":dogs

    }
    return render(request,'hod_templates/view_dog.html',context)





