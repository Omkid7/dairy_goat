from random import randrange
from unicodedata import category, name
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .forms import *
from .models import *


@login_required
def clerkHome(request):
    handler=Handler.objects.all().count()
    total_dogs=Dog.objects.all().count()
    prescip = Prescription.objects.all().count()
    doctors=Doctor.objects.all().count()

    boxer=Dog.objects.filter(category__name__contains='Boxer').count()
    boxer=int(boxer)
    print("Number of boxer is", boxer)
    
     
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
    
    rotteler=Dog.objects.filter(category__name__contains='rotteler').count()
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
        "handlers":handler,
        "breed_list":breed_list,
        "num_list": num_list,
        "total_dogs": total_dogs,
        "train_list": train_list,
        "train_num": train_num,
        "class_list":class_list,
        "class_num_list": class_num_list,
        "weight_list": weight_list,
        "weight_num": weight_num,
        "prescip": prescip,
        "doctors": doctors,
        

    }
    return render(request,'clerk_templates/clerk_home.html',context)



@login_required
def receptionistProfile(request):
    customuser = CustomUser.objects.get(id=request.user.id)
    staff = Clerk.objects.get(admin=customuser.id)

    form=ClerkForm()
    if request.method == "POST":
       

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone_number=request.POST.get('phone_number')

      
        customuser = CustomUser.objects.get(id=request.user.id)
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.save()

        staff = Clerk.objects.get(admin=customuser.id)
        form=ClerkForm(request.POST,request.FILES,instance=staff)

        staff.address = address
        staff.phone_number=phone_number
        staff.save()
        if form.is_valid():
            form.save()
        

    context={
        "form":form,
        "staff":staff,
        'user':customuser
    }
      

    return render(request,'clerk_templates/clerk_profile.html',context)


    
@login_required
def createHandler(request):
    form=HandlerForm(request.POST, request.FILES)
    try:
        if request.method == "POST":
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
            
        
            user = CustomUser.objects.create_user(username=username, email=email,password=password, first_name=first_name, last_name=last_name,user_type=5)
            user.handler.address = address
            user.handler.phone_number = phone_number
            user.handler.dob=dob
            user.handler.gender=gender
            user.save()

            messages.success(request, "Handler Added Successfully!")
            return redirect('manage_handler')
            
    except:
        
        messages.error(request,'Handler Not Saved')
        return redirect('handler_form2')
    context={
        "form":form
    }
       
    return render(request,'clerk_templates/add_handler.html',context)


@login_required
def allHandler(request):
    handler=Handler.objects.all()

    context={
        "handler":handler,

    }
    return render(request,'clerk_templates/manage_handler.html',context)

@login_required
def Location(request):
    location=Location.objects.all()

    context={
        "location":location,

    }
    return render(request,'clerk_templates/location.html',context)



@login_required
def editHandler(request,handler_id):
    request.session['handler_id'] = handler_id

    handler = Handler.objects.get(admin=handler_id)

    form = EditHandlerForm()
    

    form.fields['email'].initial = handler.admin.email
    form.fields['username'].initial = handler.admin.username
    form.fields['first_name'].initial = handler.admin.first_name
    form.fields['last_name'].initial = handler.admin.last_name
    form.fields['address'].initial = handler.address
    form.fields['gender'].initial = handler.gender
    form.fields['phone_number'].initial = handler.phone_number
    form.fields['dob'].initial = handler.dob
    try:
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
                    user = CustomUser.objects.get(id=handler_id)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.username = username
                    user.save()

                    handler_edit = Handler.objects.get(admin=handler_id)
                    handler_edit.address = address
                    handler_edit.gender = gender
                    handler_edit.dob=dob
                    handler_edit.phone_number=phone_number
                    
                    handler_edit.save()
                    messages.success(request, "handler Updated Successfully!")
                    return redirect('all_handler2')
                except:
                    messages.error(request, "Failed to Update handler.")
                    return redirect('all_handler2')
    except:
         messages.error(request, "Invalid Error!")
         return redirect('all_handler')


    context = {
        "id": handler_id,
        "form": form
    }
    return render(request, "clerk_templates/edit_handler.html", context)


       

@login_required
def handler_personalRecords(request,pk):
    handler=Handler.objects.get(id=pk)
    # prescrip=handler.prescription_set.all()

    context={
        "handler":handler,
        # "prescription":prescrip

    }
    return render(request,'clerk_templates/handler_personalRecords.html',context)


@login_required
def confirmDelete(request,pk):
    try:
        handler=Handler.objects.get(id=pk)
        if request.method == 'POST':
            handler.delete()
            messages.success(request, "Staff  deleted")

            return redirect('all_handler2')
    except:
        messages.error(request, "Handler Cannot be deleted  deleted , Handler is still on medication or an error occured")
        return redirect('all_handler2')

    context={
        "handler":handler,

    }
    
    return render(request,'clerk_templates/delete_handler.html',context)

@login_required
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
    return render(request,'clerk_templates/add_dog.html',context)

def deletedog(request,pk):
    try:
        dogs=Dog.objects.get(id=pk)
        if request.method == 'POST':
            dogs.delete()
            return redirect('all_handler')
    except:
        messages.error(request, "Handlers Cannot be deleted, Handlers is still on medication or an error occured")
        return redirect('all_handler')

    context={
        "dogs":dogs,

     }
    
    return render(request,'clerk_templates/sure_delete.html',context)




def editDog(request,pk):
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
                return redirect('manage_dog')
            except:
                messages.error(request,'An Error Was Encounterd Dog Not Updated')


        
    context={
        "dogs":dogs,
         "form":form,
         "title":"Edit Dog"

    }
    return render(request,'clerk_templates/edit_dog.html',context)


def dogDetails(request,pk):
    dog=Dog.objects.get(id=pk)
    # prescrip=Dogs.prescription_set.all()
    # Dogs=Dogs.dispense_set.all()

    context={
        "dog":dog,
        # "prescription":prescrip,
        # "Dogs":Dogs

    }
    return render(request,'clerk_templates/view_dog.html',context)


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
    return render(request,'clerk_templates/add_category.html',context)

def addClassification(request):
    try:
        form=ClassificationForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Classification added Successfully!")

                return redirect('add_classication')
    except:
        messages.error(request, "Classification Not added! Try again")

        return redirect('add_classification')

    
    context={
        "form":form,
        "title":"Add a New Breed"
    }
    return render(request,'clerk_templates/add_classification.html',context)


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
    return render(request,'clerk_templates/add_owner.html',context)


@login_required
def manageDog(request):
    Dogs = Dog.objects.all().order_by("-id")
    ex=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True)
    eo=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=False)
    

    context = {
        "Dogs": Dogs,
        "expired":ex,
        "expa":eo,
        "title":"Manage Available Dogs"
    }

    return render(request,'clerk_templates/manage_dog.html',context)


def createIncharge(request):

    if request.method == "POST":
           
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
           
        try:
            user = CustomUser.objects.create_user(username=username, email=email,password=password, first_name=first_name, last_name=last_name,user_type=6)
            user.incharge.address = address
            user.incharge.mobile = mobile

            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('manage_incharge')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_incharge')

    context = {
        "title":"Add Incharge"

    }
    

    return render(request,'clerk_templates/add_incharge.html',context)

def manageIncharge(request):
    staffs = Incharge.objects.all()

    context = {
        "staffs": staffs,
        "title":"Icharge Details"

    }

    return render(request,'clerk_templates/manage_incharge.html',context)

def deleteIncharge(request,pk):
    try:
        incharge=Incharge.objects.get(id=pk)
        if request.method == 'POST':
            incharge.delete()
            messages.success(request, "Incharge  deleted successfully")

            return redirect('manage_incharge')

    except:
        messages.error(request, "Veterinary aready deleted")
        return redirect('manage_incharge')


   
    return render(request,'clerk_templates/sure_delete.html')


def editIncharge(request,incharge_id):
    incharge = Incharge.objects.get(admin=incharge_id)
    if request.method == "POST":
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

            # INSERTING into Customuser Model
        user = CustomUser.objects.get(id=incharge_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()
        
        # INSERTING into Staff Model
        incharge = Incharge.objects.get(admin=incharge_id)
        incharge.address = address
        incharge.save()

        messages.success(request, "Staff Updated Successfully.")

    context = {
        "staff": incharge,
        "title":"Edit Incharge"
    }
    return render(request, "clerk_templates/edit_incharge.html", context)



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
    

    return render(request,'clerk_templates/add_doctor.html',context)

def manageDoctor(request):
    staffs = Doctor.objects.all()

    context = {
        "staffs": staffs,
        "title":"Veterinary Details"

    }

    return render(request,'clerk_templates/manage_doctor.html',context)

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


   
    return render(request,'clerk_templates/sure_delete.html')


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
    return render(request, "clerk_templates/edit_doctor.html", context)
