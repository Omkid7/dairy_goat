from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseRedirect
from .forms import *
from .models import *


@login_required
def pharmacistHome(request):
    handlers_total=Handler.objects.all().count()
    exipred=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True).count()
 
    out_of_dog=Dog.objects.filter(svc_age__lte=0).count()
    total_dog=Dog.objects.all().count()

    context={
        "handlers_total":handlers_total,
        "expired_total":exipred,
        "out_of_dog":out_of_dog,
        "total_dogs":total_dog,
        
    }
    return render(request,'pharmacist_templates/pharmacist_home.html',context)

@login_required
def userProfile(request):
    staff=Pharmacist.objects.all()
    form=CustomerForm()
    if request.method == "POST":
       

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

      
        customuser = CustomUser.objects.get(id=request.user.id)
        customuser.first_name = first_name
        customuser.last_name = last_name
        
        customuser.save()
        staff = Pharmacist.objects.get(admin=customuser.id)
        form=CustomerForm(request.POST,request.FILES,instance=staff)

        staff.address = address
        if form.is_valid():
            form.save()
        staff.save()
        
        messages.success(request, "Profile Updated Successfully")
        return redirect('pharmacist_profile')

    context={
        "staff":staff,
        "form":form
    }
      

    return render(request,'pharmacist_templates/staff_profile.html',context)

def manageHandlersPharmacist(request):
   
    handler=Handlers.objects.all()
    context={
        "handlers":handler
    }
    return render(request,'pharmacist_templates/manage_handlers.html',context)


def managePrescription(request):
    precrip=Dispense.objects.all()

    context={
        "prescrips":precrip,
    }
    return render(request,'pharmacist_templates/handler_prescrip.html',context)


    
def manageDog(request):
    dogs = Dog.objects.all()
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

    }
    return render(request,'pharmacist_templates/manage_dog.html',context)


def manageDispense(request,pk):
    queryset=Handler.objects.get(id=pk)
    prescrips=queryset.prescription_set.all()
    
    print(prescrips)
    form=DispenseForm(request.POST or None,initial={'handler_id':queryset} )
    dogs=Dog.objects.all()
    ex=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=True)
    eo=Dog.objects.annotate(
    expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
    ).filter(expired=False)
    # print(ex)
      
   
    try:  
        
        if request.method == 'POST':
            if form.is_valid(): 
                username = form.cleaned_data['taken']
                qu=form.cleaned_data['dispense_svc_age']
                ka=form.cleaned_data['dog_id']
                # print(username)
            
            
                    
                dog= eo=Dog.objects.annotate(
                expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
                ).filter(expired=False).get(id=username)
                form=DispenseForm(request.POST or None, instance=dog)
                instance=form.save()
                # print(instance)
                instance.svc_age-=qu
                instance.save()

                form=DispenseForm(request.POST or None ,initial={'handler_id':queryset})
                form.save()

                messages.success(request, "Dog Has been Successfully Deployed")

                return redirect('manage_handler_pharmacist')
            else:
                messages.error(request, "Validty Error")

                return redirect('manage_handler_pharmacist')

        context={
            "handlers":queryset,
            "form":form,
            # "Dogs":Dog,
            "dogs":dogs,
            "prescrips":prescrips,
            "expired":ex,
            "expa":eo,

            }
        if request.method == 'POST':
        
            print(dogs)
            context={
                "dogs":dogs,
                form:form,
                "prescrips":prescrips,
                "handlers":queryset,
                "expired":ex,
                "expa":eo,

            }
    except:
        messages.error(request, "Deployed Not Allowed! The Dog has reached ROD ,please contact the admin for more dogs  ")
        return redirect('manage_handler_pharmacist')
    context={
            "handlers":queryset,
            "form":form,
            # "Dogs":Dog,
            "dogs":dogs,
            "prescrips":prescrips,
            "expired":ex,
            "expa":eo,
            }
    
    return render(request,'pharmacist_templates/manage_dispense.html',context)



def handler_feedback_message(request):
    feedbacks = HandlersFeedback.objects.all()
    context = {
        "feedbacks": feedbacks
    }
    return render(request, 'pharmacist_templates/handler_feedback.html', context)

@csrf_exempt
def handler_feedback_message_reply(request):
    feedback_id = request.POST.get('id')
    feedback_reply = request.POST.get('reply')
    try:
        feedback =  HandlerFeedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        return HttpResponse("True")

    except:
        return HttpResponse("False")

def deletefeedback(request,pk):
    try:
        fed=HandlerFeedback.objects.get(id=pk)
        if request.method == 'POST':
            fed.delete()
            messages.success(request, "Feedback  deleted successfully")
            return redirect('handler_feedback_message')

    except:
        messages.error(request, "Feedback Error, Please Check again")
        return redirect('handler_feedback_message')


   
    return render(request,'pharmacist_templates/sure_delete.html')
    



def dogDetails(request,pk):
    dogs=Dog.objects.get(id=pk)
    context={
        "dogs":dogs,
       

    }
    return render(request,'pharmacist_templates/view_dog.html',context)



def deleteDispense4(request,pk):
    try:
        fed=Dispense.objects.get(id=pk)
        if request.method == 'POST':
            fed.delete()
            messages.success(request, "Deployment  deleted successfully")
            return redirect('pharmacist_prescription')

    except:
        messages.error(request, "Delete Error, Please Check again")
        return redirect('pharmacist_prescription')


   
    return render(request,'pharmacist_templates/sure_delete.html')
    








































































# # def dispensedog(request,pk):
# #     queryset=handlers.objects.get(id=pk)
# #     form=DispenseForm(initial={'handler_id':queryset})
# #     if request.method == 'POST':
# #         form=DispenseForm(request.POST or None)
# #         if form.is_valid():
# #             form.save()
            
    
# #     context={
# #         # "title":' Issue' + str(queryset.item_name),
# #         "queryset":queryset,
# #         "form":form,
# #         # "username":" Issue By" + str(request.user),
# #     }
# #     return render(request,"pharmacist_templates/dispense_dog.html",context)

# # def manageDispense(request):
# #     disp=De.objects.all()
# #     context={
# #         "prescrips":disp,
# #     }
# #     return render(request,'pharmacist_templates/manage_dispense.html',context)




# def dispense(request,pk):
#     queryset=dog.objects.get(id=pk)
#     form=DispenseForm2(request.POST or None,instance=queryset)
#     if form.is_valid():
#         instance=form.save(commit=False)
#         instance.svc_age-=instance.dispense_svc_age
#         print(instance.dog_id.svc_age)
#         print(instance.dispense_svc_age)
#         instance.save()

#         return redirect('pharmacist_disp')

       
    
#     context={
#         "queryset":queryset,
#         "form":form,
#     }
#     return render(request,'pharmacist_templates/dispense_form.html',context)

