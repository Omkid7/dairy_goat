from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from .decorators import *
from django.views.generic.base import TemplateView
from django.db.models import Count


from .forms import *
from .models import *

# class MarkersMapView(TemplateView):
#     """Markers map view."""

#     template_name = "doctor_home.html"

def doctorHome(request): 
    prescip = Prescription.objects.all().count()
    total_dogs=Dog.objects.all().count()
    total_handlers=Handler.objects.all().count()
    
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
    
    
    train_list=['Scounting', 'Controlled', 'Utilization', 'Leashing']
    train_num=[scounting,controlled,utilization,leash]
    
    breed_list=['bulldog', 'Boxer', 'Labrador Retriever','Wrotteler', 'German Shepherd']
    num_list=[bulldog, boxer, rotteler, labrador, german]
    
    class_list=['Explosive', 'Protection Dog', 'Infantry Patrol Dogs','Explosive Search Dogs', 'Human Detection Dogs(U/T)', 'Narcotic Dogs', 'Patrol and Search Dogs' ]
    class_num_list=[explosive, protection, infantry, explosive_search, human, narcotic, patrol ]
    exipred=Vaccination.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True).count()
    
    weight=MonthlyBody.objects.filter(weight__gte='30')
    print("the weight is", weight)
    
    
    

    context={
        "Prescription_total":prescip,
        "breed_list":breed_list,
        "num_list": num_list,
        "train_list":train_list,
        "train_num":train_num,
        "class_list":class_list,
        "class_num_list": class_num_list,
        "total_dogs": total_dogs,
        "total_dogs": total_dogs,
        "expired": exipred,
        "vaccine_list": vaccine_list,
        "num_vac": num_vac,
        "weight": weight
      
      
        

    }
    return render(request,'veterinary_templates/doctor_home.html',context)

def doctorProfile(request):
    customuser=CustomUser.objects.get(id=request.user.id)
    staff=Doctor.objects.get(admin=customuser.id)

    form=DoctorForm()
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')


        customuser=CustomUser.objects.get(id=request.user.id)
        customuser.first_name=first_name
        customuser.last_name=last_name
        customuser.save()

        staff=Doctor.objects.get(admin=customuser.id)
        form =DoctorForm(request.POST,request.FILES,instance=staff)

        staff.save()

        if form.is_valid():
            form.save()

    context={
        "form":form,
        "staff":staff,
   
    }

    return render(request,'veterinary_templates/doctor_profile.html',context)

def manageDogs(request):
    dogs=Dog.objects.all()

    context={
        "dogs":dogs,

    }
    return render(request,'veterinary_templates/manage_dogs.html',context)

def addPrescription(request,pk):        
    dog=Dog.objects.get(id=pk)
    form=PrescriptionForm(
        initial={'dog_id':dog,
                 'category': dog,
                 'dog_imprint': dog,
                 'svc_no':dog,
                 'quantity': dog,
                 'manufacture':dog,
                 'vaccination_id':dog,
                 
                 }
        )
    if request.method == 'POST':
        try:
            form=PrescriptionForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request,'Prescription added successfully')
                return redirect('manage_precrip_doctor')
        except:
            messages.error(request,'Prescription Not Added')
            return redirect('manage_dogs')


    context={
        "form":form,
        "dog":dog    
    }
    return render(request,'veterinary_templates/prescribe_form.html',context)

def dog_personalDetails(request,pk):
    dog=Dog.objects.get(id=pk)
    prescrip=Prescription.objects.all()

    context={
        "dog":dog,
        "prescription":prescrip

    }
    return render(request,'veterinary_templates/dog_personalRecords.html',context)


def deletePrescription(request,pk):
    prescribe=Prescription.objects.get(id=pk)

    if request.method == 'POST':
        try:
            prescribe.delete()
            messages.success(request,'Prescription Deleted successfully')
            return redirect('manage_precrip_doctor')
        except:
            messages.error(request,'Prescription Not Deleted successfully')
            return redirect('manage_precrip_doctor')




    context={
        "dog":prescribe
    }

    return render(request,'veterinary_templates/sure_delete.html',context)

def deleteMonthlyWeight(request,pk):
    body=MonthlyBody.objects.get(id=pk)

    if request.method == 'POST':
        try:
            body.delete()
            messages.success(request,'Monthly Body Weight Deleted successfully')
            return redirect('manage_weight')
        except:
            messages.error(request,'Monthly Body Weight Not Deleted successfully')
            return redirect('manage_weight')




    context={
        "body":body
    }

    return render(request,'veterinary_templates/monthly_delete.html',context)




def viewMonthlyWeight(request, pk):
    body=MonthlyBody.objects.get(id=pk)
  

    context={
        "body": body,
        "title": "View Monthly Body Weight"
    }
    
    return render(request, 'veterinary_templates/view_monthly_weight.html', context)
    
def managePrescription(request):
    precrip=Prescription.objects.all().order_by("-id")
    ex=Prescription.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True)
    eo=Prescription.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=False)

    dog = Dog.objects.all()
    
       
    context={
        "prescrips":precrip,
        "dog":dog,
        "expired": ex,
        "expa": eo
    }
    return render(request,'veterinary_templates/manage_prescription.html' ,context)



def editPrescription(request,pk):
    prescribe=Prescription.objects.get(id=pk)
    form=PrescriptionForm(instance=prescribe)

    
    if request.method == 'POST':
        form=PrescriptionForm(request.POST ,instance=prescribe)

        try:
            if form.is_valid():
                form.save()

                messages.success(request,'Prescription Updated successfully')
                return redirect('manage_precrip_doctor')
        except:
            messages.error(request,' Error!! Prescription Not Updated')
            return redirect('manage_precrip_doctor')




    context={
        "dog":prescribe,
        "form":form
    }

    return render(request,'veterinary_templates/edit_prescription.html',context)


def add_Monthly_Weight(request):
    try:
        form=MonthlyForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Monthly Body Weight added Successfully!")

                return redirect('manage_weight')
    except:
        messages.error(request, "Monthly Body Weight Not added! Try again")

        return redirect('manage_weight')

    
    context={
        "form":form,
        "title":"Add Monthly Body Weight"
    }
    return render(request,'veterinary_templates/add_body_weight.html',context)

def add_vaccine_category(request):
    try:
        form=VaccinationTypeForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Vaccination Category added Successfully!")

                return redirect('add_vaccination_category')
    except:
        messages.error(request, "Vaccination Category Not added! Try again")

        return redirect('add_vaccination_category')

    
    context={
        "form":form,
        "title":"Add Vaccination Category"
    }
    return render(request,'veterinary_templates/add_vaccination_category.html',context)

def addDeworming(request):
    try:
        form=DewormingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Deworming added Successfully!")

                return redirect('manage_deworm')
    except:
        messages.error(request, "Deworming Not added! Try again")

        return redirect('manage_deworm')

    
    context={
        "form":form,
        "title":"Add Deworming"
    }
    return render(request,'veterinary_templates/add_deworming.html',context)

def addVaccination(request):
    form=vaccinationForm(request.POST,request.FILES)
    if form.is_valid():
        form=vaccinationForm(request.POST or None)

        form.save()
        return redirect('manage_vaccination_dog')
    
    context={
        "form":form,
        "title":"Add New Vaccine dog"
    }
    return render(request,'veterinary_templates/add_vaccination.html',context)

def addLocation(request):
    form=LocationForm(request.POST,request.FILES)
    if form.is_valid():
        form=LocationForm(request.POST or None)

        form.save()
        return redirect('add_map')
    
    context={
        "form":form,
        "title":"Add New Map"
    }
    return render(request,'veterinary_templates/add_map.html',context)


def add_Type_of_Deworming(request):
    try:
        form=Type_of_DewormingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Deworming added Successfully!")

                return redirect('manage_deworm')
    except:
        messages.error(request, "Deworming Not added! Try again")

        return redirect('manage_deworm')

    
    context={
        "form":form,
        "title":"Add Type of Deworming"
    }
    return render(request,'veterinary_templates/add_type_of_deworming.html',context)





def manage_vaccination(request):
    vaccine=Vaccination.objects.all().order_by("-id")
    ex=Vaccination.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True)
    eo=Vaccination.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=False)
    
    context = {
        "vaccine": vaccine,
        "expired":ex,
        "expa":eo,
        "title":"Manage Available Vaccines"
    }

    return render(request,'veterinary_templates/manage_vaccination.html',context)

def editVaccine(request,pk):
    dogs=Vaccination.objects.get(id=pk)
    form=vaccinationForm(request.POST or None,instance=dogs)

    if request.method == "POST":
        if form.is_valid():
            form=vaccinationForm(request.POST or None ,instance=dogs)

            name=request.POST.get('name')
            quantity=request.POST.get('quantity')
            # email=request.POST.get('email')

            try:
                dogs =Vaccination.objects.get(id=pk)
                dogs.name=name
                dogs.quantity=quantity
                dogs.save()
                form.save()
                messages.success(request,'Vaccine  Updated Succefully')
            except:
                messages.error(request,'An Error Was Encounterd Vaccine Not Updated')


        
    context={
        "dogs":dogs,
         "form":form,
         "title":"Edit Vaccine"

    }
    return render(request,'veterinary_templates/edit_vaccine.html',context)
  
def deleteVaccine(request,pk):
    vaccine=Vaccination.objects.get(id=pk)

    if request.method == 'POST':
        try:
            vaccine.delete()
            messages.success(request,'Vaccine Deleted successfully')
            return redirect('manage_vaccination')
        except:
            messages.error(request,'Vaccine Not Deleted successfully')
            return redirect('manage_vaccination')




    context={
        "vaccine":vaccine
    }

    return render(request,'veterinary_templates/delete_vaccine.html',context)

def deleteDeworm(request,pk):
    vaccine=Type_of_deworming.objects.get(id=pk)

    if request.method == 'POST':
        try:
            vaccine.delete()
            messages.success(request,'Deworming Deleted successfully')
            return redirect('manage_deworm')
        except:
            messages.error(request,'Deworming Not Deleted successfully')
            return redirect('manage_deworm')

    context={
        "vaccine":vaccine
    }

    return render(request,'veterinary_templates/delete_worm.html',context)


def reorder_level(request, pk):
    queryset = Vaccination.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for " + str(instance.name) + " is updated to " + str(instance.reorder_level))

        return redirect("manage_vaccination")
    context ={
        "instance": queryset,
        "form": form,
        "title":"Reorder Level"
    }

    return render(request,'veterinary_templates/reorder_level.html',context)


  
def addDeworming(request):
    try:
        form=DewormingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Deworming added Successfully!")

                return redirect('add_deworming')
    except:
        messages.error(request, "Deworming Not added! Try again")

        return redirect('add_deworming')

    
    context={
        "form":form,
        "title":"Add Deworming"
    }
    return render(request,'veterinary_templates/add_deworming.html',context)



def editMonthlyWeight(request,pk):
    body=MonthlyBody.objects.get(id=pk)
    form=EditMonthlyForm(instance=body)

    
    if request.method == 'POST':
        form=EditMonthlyForm(request.POST ,instance=body)

        try:
            if form.is_valid():
                form.save()

                messages.success(request,'Monthly Weight Updated successfully')
                return redirect('manage_precrip_doctor')
        except:
            messages.error(request,' Error!! Prescription Not Updated')
            return redirect('manage_precrip_doctor')




    context={
        "body" :body,
        "form":form
    }

    return render(request,'veterinary_templates/edit_weight.html',context)


def manageBodyWeight(request):
    body=MonthlyBody.objects.all()    
       
    context={
        "body":body,
    }
    return render(request,'veterinary_templates/manage_weight.html' ,context)


def manageDeworming(request):
    worm=Type_of_deworming.objects.all().order_by("-id")  
    ex=Type_of_deworming.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True)
    eo=Type_of_deworming.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=False) 
    
       
    context={
        "worm":worm,
        "expired": ex,
        "expa": eo
    }
    return render(request,'veterinary_templates/manage_deworm.html' ,context)
    