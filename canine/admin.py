from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Location, LeafletGeoAdmin)

class HandlerAdmin(admin.ModelAdmin):
    list_display = ('admin','gender')
    search_fields = ["admin__username"]
class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser, UserModel)
admin.site.register(Handler,HandlerAdmin)
admin.site.register(Pharmacist)
admin.site.register(AdminHOD)
admin.site.register(Dog)
admin.site.register(Incharge)
admin.site.register(Category)
admin.site.register(Doctor)
admin.site.register(Clerk)
admin.site.register(Prescription)
admin.site.register(Dispense)
admin.site.register(HandlerFeedback)
admin.site.register(Unit)
admin.site.register(Certification)
admin.site.register(Mwt)
admin.site.register(Course)
admin.site.register(Training)
admin.site.register(WeaponTraining)
admin.site.register(ScoutingTraining)
admin.site.register(ControlledTraining)
admin.site.register(Utilization)
admin.site.register(LeashTraining)
admin.site.register(Training_day_session)
admin.site.register(MonthlyBody)
admin.site.register(Deworming)
admin.site.register(Type_of_deworming)
admin.site.register(Vaccination)
admin.site.register(Classification)
admin.site.register(VaccinationCategory)
# admin.site.register(Type_of_vaccine)









   



 



