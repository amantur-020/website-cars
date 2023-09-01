from django.contrib import admin
from .models import *

# Админка машины
@admin.register(CarsBrand)
class CarsBrandAdmin(admin.ModelAdmin):
    list_display=("name",)
    list_filter=("name",)



@admin.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    list_display=("brand","model",)
    list_filter=("brand",)
    search_fields=("brand__name",)



@admin.register(CarsColors)
class CarsColorAdmin(admin.ModelAdmin):
    list_display=("color",)
    list_filter=("color",)
    search_fields=("color",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display=("name",)



@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display=("cars","date","year","currency","price","mileage","colors","kpp","wd","steering_weel","carcase","fuel","state","vin","engine_volumes","description",)
    list_filter=("cars__brand__name","year","price","colors","kpp","wd","steering_weel","carcase","fuel","state","vin","engine_volumes",)
    search_fields=("cars__brand__name",)





#Админка мотоцикла
@admin.register(MotorbikeBrand)
class MotorbikeBrandAdmin(admin.ModelAdmin):
    list_display=("name",)
    list_filter=("name",)
    search_fields=("name",)




@admin.register(MotobikeModel)
class MotobikeModelAdmin(admin.ModelAdmin):
    list_display=("brand","model",)
    list_filter=("brand",)
    search_fields=("brand__name",)



@admin.register(Motobike)
class MotobiekAdmin(admin.ModelAdmin):
    list_display=("motobike","year","engine_volumes","mileage","state","price","engine","fuel","class_moto",)
    list_filter=("motobike__brand__name","year","engine_volumes","state","price","fuel","class_moto")
    search_fields=("motobike__brand__name",)




#Админка пользователей
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display=("name","phone",)



#Админка запчастей
@admin.register(SpareParts)
class SparePartsAdmin(admin.ModelAdmin):
    list_display=("name","state","country","code","model","description")