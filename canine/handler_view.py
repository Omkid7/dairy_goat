from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import *
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


@login_required
def handlerHome(request):
    handler_obj = Handler.objects.get(admin=request.user.id)
    dog=Dog.objects.all().count()
    handler_dispen=handler_obj.dispense_set.all().count()
    prescip = Prescription.objects.all().count()

      
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
          "prescip": prescip,
          "total_disp":handler_dispen,
          "dog": dog,
          "breed_list":breed_list,
          "num_list": num_list,
          "train_list":train_list,
          "train_num":train_num,
          "class_list":class_list,
          "class_num_list": class_num_list,
          "dog_weight": dog_weight,
          "weight_list": weight_list,
          "weight_num":weight_num
     }
    return render(request,'handler_templates/handler_home.html',context)

@login_required
def handlerProfile(request):
    customuser = CustomUser.objects.get(id=request.user.id)
    patien = Handler.objects.get(admin=customuser.id)
   
    form=HandlerPicForm1()
    if request.method == "POST":
       

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')

      
        customuser = CustomUser.objects.get(id=request.user.id)
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.email=email
        
        customuser.save()
        hanlder = Handler.objects.get(admin=customuser.id)
        form=HandlerPicForm1(request.POST,request.FILES,instance=patien)

        patien.address = address
        if form.is_valid():
            form.save()
        patien.save()
       
        messages.success(request, "Profile Updated Successfully")
        return redirect('handler_profile')

    context={
        "patien":patien,
        "form":form
    }
      

    return render(request,'handler_templates/handler_profile.html',context)



def addLeashTraining(request):
    try:
        form=LeashTrainingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Information added Successfully!")

                return redirect('all_leash_training')
    except:
        messages.error(request, "Information Not added! Try again")

        return redirect('all_leash_training')

    
    context={
        "form":form,
        "title":"Add Leash Training"
    }
    return render(request,'handler_templates/leash_training.html',context)

def handler_remarks(request, pk):
    queryset = LeashTraining.objects.get(id=pk)
    form = LeashRemarksForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Remarks added successfully")

        return redirect("all_leash_training")
    context ={
        "instance": queryset,
        "form": form,
        "title":"Add Remarks"
    }

    return render(request,'handler_templates/add_leash_remarks.html',context)


def editLeashTraining(request, pk):
    train=LeashTraining.objects.get(id=pk)
    form=LeashTrainingForm(request.POST or None, instance=train)
    
    if request.method == "POST":
        if form.is_valid():
            form=LeashTrainingForm(request.POST or None , instance=train)
            leash=request.POST.get('leash')
            
            try:
                train=LeashTraining.objects.get(id=pk)
                train.leash=leash
                train.save()
                form.save()
                messages.success(request, 'Information Updated Successfully')
                return redirect('all_leash_training')
            except:
                messages.error(request, 'Information Not Updates')
                
    context={
        "train": train,
        "form": form,
        "title":"Edit Leash Training"
    }
    return render(request, 'handler_templates/edit_leash_training.html', context)


def delete_LeashTraining(request, pk):
    try:
        train=LeashTraining.objects.get(id=pk)
        if request.method == 'POST':
            train.delete()
            messages.success(request, 'Information deleted successfully')
            
            return redirect('all_leash_training')
    except:
        messages.error(request, 'Leash already deleted')
        return redirect('all_leash_training')
    
    return render(request, 'handler_templates/delete_leash_train.html')

def viewLeashTraining(request, pk):
    leash=LeashTraining.objects.get(id=pk)
    context={
        "leash": leash,
        "title": "View Leash Training"
    }
    
    return render(request, 'handler_templates/view_leash_train.html', context)


def viewControlledTraining(request, pk):
    control=ControlledTraining.objects.get(id=pk)
    context={
        "control": control,
        "title": "View Controlled Training"
    }
    
    return render(request, 'handler_templates/view_controlled_train.html', context)

def viewScoutTraining(request, pk):
    scout=ScoutingTraining.objects.get(id=pk)
    context={
        "scout": scout,
        "title": "View Scounting Training"
    }
    
    return render(request, 'handler_templates/view_scout_train.html', context)

def manage_LeashTraining(request):
    train=LeashTraining.objects.all()
    context={
        "train": train,
        "title": "Manage Leash Training"
    }
    
    return render(request, 'handler_templates/all_leash_training.html', context)

def add_controlled_Training(request):
    try:
        form=ControlledTrainingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Information added Successfully!")

                return redirect('all_controlled_training')
    except:
        messages.error(request, "Information Not added! Try again")

        return redirect('all_controlled_training')

    
    context={
        "form":form,
        "title":"Add Controlled Training"
    }
    return render(request,'handler_templates/controlled_training.html',context)


def editControlledTraining(request, pk):
    train=ControlledTraining.objects.get(id=pk)
    form=ControlledTrainingForm(request.POST or None, instance=train)
    
    if request.method == "POST":
        if form.is_valid():
            form=ControlledTrainingForm(request.POST or None , instance=train)
            dog=request.POST.get('dog')
       
            
            try:
                train=ControlledTraining.objects.get(id=pk)
                train.dog=dog
                train.save()
                form.save()
                messages.success(request, 'Information Updated Successfully')
            except:
                messages.error(request, 'Information Updated Successfully')
                
    context={
        "train": train,
        "form": form,
        "title":"Edit Controlled Training"
    }
    return render(request, 'handler_templates/edit_controlled_training.html', context)


def delete_ControlledTraining(request, pk):
    try:
        train=ControlledTraining.objects.get(id=pk)
        if request.method == 'POST':
            train.delete()
            messages.success(request, 'Information deleted successfully')
            
            return redirect('all_controlled_training')
    except:
        messages.error(request, 'Controlled already deleted')
        return redirect('all_controlled_training')
    
    return render(request, 'handler_templates/delete_controlled_train.html')


def manage_ControlledTraining(request):
    train=ControlledTraining.objects.all()
    context={
        "train": train,
        "title": "Manage Controlled Training"
    }
    
    return render(request, 'handler_templates/all_controlled_training.html', context)


# Scouting training
def add_ScountingTraining(request):
    try:
        form=ScountingTrainingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Information added Successfully!")

                return redirect('all_scounting_training')
    except:
        messages.error(request, "Information Not added! Try again")

        return redirect('all_scounting_training')

    
    context={
        "form":form,
        "title":"Add Controlled Training"
    }
    return render(request,'handler_templates/scounting_training.html',context)



def add_HandlerRemarks(request):
    
    try:
        form=HandlerForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Information added Successfully!")

                return redirect('view_handlers')
    except:
        messages.error(request, "Information Not added! Try again")

        return redirect('view_handlers')

    
    context={
        "form":form,
        "title":"Add Remarks on Training"
    }
    return render(request,'handler_templates/handlers_remarks.html',context)


def editScountingTraining(request, pk):
    train=ScoutingTraining.objects.get(id=pk)
    form=ScountingTrainingForm(request.POST or None, instance=train)
    
    if request.method == "POST":
        if form.is_valid():
            form=ScountingTrainingForm(request.POST or None , instance=train)
            dog=request.POST.get('dog')
          
            
            try:
                train=ScoutingTraining.objects.get(id=pk)
                train.dog=dog
                train.save()
                form.save()
                messages.success(request, 'Information Updated Successfully')
            except:
                messages.error(request, 'Information Updated Successfully')
                
    context={
        "train": train,
        "form": form,
        "title":"Edit Training"
    }
    return render(request, 'handler_templates/edit_scounting_training.html', context)


def delete_ScountingTraining(request, pk):
    try:
        train=ScoutingTraining.objects.get(id=pk)
        if request.method == 'POST':
            train.delete()
            messages.success(request, 'Information deleted successfully')
            
            return redirect('all_scounting_training')
    except:
        messages.error(request, 'Scounting already deleted')
        return redirect('all_scounting_training')
    
    return render(request, 'handler_templates/delete_scounting_train.html')


def manage_ScountingTraining(request):
    train=ScoutingTraining.objects.all()
    context={
        "train": train,
        "title": "Manage Scounting Training"
    }
    
    return render(request, 'handler_templates/all_scounting_training.html', context)



def addHandlerScores(request):
    form=HandlerScoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_handlers_scores')
    
    context={
        "form":form,
        "title":"Add Handlers"
    }
    return render(request,'handler_templates/add_handlers_scores.html',context)


def viewHandlersScores(request, pk):
    handler=HandlerScores.objects.get(id=pk)
    context={
        "train": handler,
        "title": "View Weapon Training"
    }
    
    return render(request, 'handler_templates/view_handler_scores.html', context)

def manage_ScountingTraining(request):
    train=ScoutingTraining.objects.all()
    context={
        "train": train,
        "title": "Manage Scounting Training"
    }
    
    return render(request, 'handler_templates/all_scounting_training.html', context)

def manage_Handlers_scores(request):
    train=HandlerScores.objects.all()
    context={
        "train": train,
        "title": "Manage Handlers Scores"
    }
    
    return render(request, 'handler_templates/all_handlers_scores.html', context)




def addWeaponTraining(request):
    try:
        form=WeaponTrainingForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Information added Successfully!")

                return redirect('all_weapon_training')
    except:
        messages.error(request, "Information Not added! Try again")

        return redirect('all_weapon_training')

    
    context={
        "form":form,
        "title":"Add Weapon Training"
    }
    return render(request,'handler_templates/add_weapon_training.html',context)


def editWeaponTraining(request, pk):
    train=WeaponTraining.objects.get(id=pk)
    form=WeaponTrainingForm(request.POST or None, instance=train)
    
    if request.method == "POST":
        if form.is_valid():
            form=WeaponTrainingForm(request.POST or None , instance=train)
            dog=request.POST.get('dog')
            onleash=request.POST.get('onleash')
            offleash=request.POST.get('offleash')
            
            try:
                train=WeaponTraining.objects.get(id=pk)
                train.dog=dog
                train.onleash=onleash
                train.offleash=offleash
                train.save()
                form.save()
                messages.success(request, 'Information Updated Successfully')
            except:
                messages.error(request, 'Information Updated Successfully')
                
    context={
        "train": train,
        "form": form,
        "title":"Edit Training"
    }
    return render(request, 'handler_templates/edit_weapon_training.html', context)
 
 
 
def delete_WeaponTraining(request, pk):
    try:
        train=WeaponTraining.objects.get(id=pk)
        if request.method == 'POST':
            train.delete()
            messages.success(request, 'Information deleted successfully')
            
            return redirect('all_weapon_training')
    except:
        messages.error(request, 'Training already deleted')
        return redirect('all_weapon_training')
    
    return render(request, 'handler_templates/delete_weapon_train.html')



def manage_Weapon_Training(request):
    train=WeaponTraining.objects.all()
    context={
        "train": train,
        "title": "Manage Type of Training"
    }
    
    return render(request, 'handler_templates/all_weapon_training.html', context)



def viewTraining(request, pk):
    train=WeaponTraining.objects.get(id=pk)
    context={
        "train": train,
        "title": "View Weapon Training"
    }
    
    return render(request, 'handler_templates/view_weapon_training.html', context)

    
def utilization(request):
    try:
        form=UtilizationForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Information added Successfully!")

                return redirect('manage_utilization')
    except:
        messages.error(request, "Information Not added! Try again")

        return redirect('manage_utilization')

    
    context={
        "form":form,
        "title":"Utilization"
    }
    return render(request,'handler_templates/utilization.html',context)


def allUtilizaation(request):
    utilize=Utilization.objects.all()
    context={
        "utilize": utilize,
        "title": "Manage Type of Training"
    }
    
    return render(request, 'handler_templates/manage_utilization.html', context)


def editUtilization(request,pk):
    utilize=Utilization.objects.get(id=pk)
    form=UtilizationForm(request.POST or None, instance=utilize)
    if request.method=="POST":
        if form.is_valid():
            dog=request.POST.get('dog')
            
            try:
                utilize=Utilization.objects.get(id=pk)
                utilize.dog=dog
                utilize.save()
                form.save()
                messages.success(request, 'Utilization Information Added successfully')
            except:
                messages.error(request, 'Utilization Information not Added successfully')
                
    context={
        "utilize": utilize,
        "form": form
    }
    
    return render(request, 'handler_templates/edit_utilization.html', context)


def deleteUtilization(request,pk):
    try:
        utilize=Utilization.objects.get(id=pk)
        if request.method=='POST':
            utilize.delete()
            messages.success(request, 'Utilization information deleted successfully')
            
            return redirect('manage_utilization')
    except:
        messages.error(request, 'Utilzation already Deleted')
        return redirect('manage_training')
    return render(request, 'handler_templates/delete_utilization.html')
    
   
def viewUtilization(request, pk):
    utilize=HandlerScores.objects.get(id=pk)
    context={
        "utilize": utilize,
        "title":"View Utilization"
    }
    
    return render(request, 'handler_templates/view_utilization.html', context)


def handler_remarks(request, pk):
    queryset = HandlerScores.objects.get(id=pk)
    form = HandlerForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Remarks added successfully")

        return redirect("manage_utilization")
    context ={
        "instance": queryset,
        "form": form,
        "title":"Add Remarks"
    }

    return render(request,'handler_templates/add_remarks.html',context)

 
    
def myPrescription(request):
    precrip=Prescription.objects.all()

    handler = Handler.objects.all()


    context={
        "prescrips":precrip,
        "handler":handler
    }
    return render(request,'veterinary_templates/myprescription.html' ,context)


def myPrescriptionDelete(request):
    handler_obj = Handler.objects.get(admin=request.user.id)
    precrip=handler_obj.prescription_set.all()
    if request.method == "POST":
        precrip.delete()




    context={
        "prescrips":precrip,
    }
    return render(request,'handler_templates/sure_delete.html',context)

def handler_feedback(request):
    handler_fed = Handler.objects.get(admin=request.user.id)
    feedback = HandlerFeedback.objects.filter(handler_id=handler_fed)
    context = {
        "feedback":feedback
    }
    return render(request, "handler_templates/handler_feedback.html", context)


def handler_feedback_save(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback_message')
        staff_obj = Handler.objects.get(admin=request.user.id)

     
        add_feedback =HandlerFeedback(handler_id=staff_obj, feedback=feedback, feedback_reply="")
        add_feedback.save()
        messages.success(request, "Feedback Sent.")
        return redirect('handler_feedback')

def handlerdeletefeedback(request,pk):
    try:
        fed=HandlerFeedback.objects.get(id=pk)
        if request.method == 'POST':
            fed.delete()
            messages.success(request, "Feedback  deleted successfully")
            return redirect('handler_feedback')

    except:
        messages.error(request, "Feedback Error, Please Check again")
        return redirect('handler_feedback')


   
    return render(request,'handler_templates/sure_delete.html')


def handler_dispense3(request):
    handler_obj = Handler.objects.get(admin=request.user.id)

    handler_dispen=handler_obj.dispense_set.all()

    context={
        "dispense":handler_dispen
    }
    return render(request, "handler_templates/handler_dispense.html", context)


