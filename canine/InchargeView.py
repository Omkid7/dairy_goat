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

def InchargeHome(request):
    handlers_total=Handler.objects.all().count()
    # categories=Dog.objects.filter(name='category').count()
    doctors=Doctor.objects.all().count()
    pharmacist=Pharmacist.objects.all().count() 
    receptionist=Clerk.objects.all().count() 
    prescip = Prescription.objects.all().count()

    out_of_Dog=Dog.objects.filter(svc_age__lte=0).count()
    total_Dog=Dog.objects.all().count()
    today = datetime.today()
    for_today = Handler.objects.filter(date_admitted__year=today.year, date_admitted__month=today.month, date_admitted__day=today.day).count()
    print(for_today)
    exipred=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True).count()
    
    
     
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
    
    breed_list=['bulldog', 'Boxer', 'Labrador Retriever','rotteler', 'German Shepherd']
    num_list=[bulldog, boxer, rotteler, labrador, german]
    
    class_list=['Explosive', 'Protection Dog', 'Infantry Patrol Dogs','Explosive Search Dogs', 'Human Detection Dogs(U/T)', 'Narcotic Dogs', 'Patrol and Search Dogs' ]
    class_num_list=[explosive, protection, infantry, explosive_search, human, narcotic, patrol ]
   
    weight_list=('Ben','Wiko', 'Dan', 'Allan')
    weight_num=(dog_weight)
   
    
    
     


    context={
        "handlers_total":handlers_total,
        "expired_total":exipred,
        "out_of_Dog":out_of_Dog,
        "total_dogs":total_Dog,
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
        "weight_num":weight_num
        
        
        # "category":category,

    }
    return render(request,'incharge_templates/incharge_home.html',context)