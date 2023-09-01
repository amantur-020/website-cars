from rest_framework import serializers
from .models import *





# Serializer машины
class CarsBrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=CarsBrand
        fields=("id","name",)


class CarsModelSerializers(serializers.ModelSerializer):
    brand=serializers.CharField(source="brand.name")
    class Meta:
        model=CarsModel
        fields=("id","brand__name","model",)


class CarsColorsSerializers(serializers.ModelSerializer):
    class Meta:
        model=CarsColors
        fields=("id","color",)


class CarsCountrySerializers(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=("id","name",)



class CarsSerializers(serializers.ModelSerializer):
    cars_model=serializers.CharField(source="cars.model")
    cars_colors=serializers.CharField(source="colors.color")
    cars_country=serializers.CharField(source="country.name")
    class Meta:
        model=Cars
        fields=(
            "id","cars_model","date","year","currency","price","mileage",
            "cars_colors","kpp","wd","steering_weel","carcase","fuel",
            "state","vin","engine_volumes","cars_country","description",
                )
        
    def create(self, validated_data):
        cars_model=validated_data.pop("cars").get("model")
        model=CarsModel.objects.get(model=cars_model)
        cars_colors=validated_data.pop("colors").get("color")
        color=CarsColors.objects.get(color=cars_colors)
        cars_country=validated_data.pop("country").get("name")    
        country=Country.objects.get(name=cars_country) 
        cars=Cars.objects.create(cars=model,colors=color,country=country)
        return cars

     






# Serializer мотоцикла
class MotobikeBramdSerializers(serializers.ModelSerializer):
    class Meta:
        model=MotorbikeBrand
        fields=("id","name",)



class MotobikeModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=MotobikeModel
        fields=("id","brand","name",)



class MotobikeSerializers(serializers.ModelSerializer):
    motobike_model=serializers.CharField(source="motobike.model")
    class Meta:
        model=Motobike
        fields=("id","motobike_model","date","year","engine_volumes",
                "mileage","state","price","engine","fuel","class_moto")
        
    def create(self, validated_data):
        motobikemodel=validated_data.pop("motobike").get("model")
        model=MotobikeModel.objects.get(model=motobikemodel)
        motobike=Motobike.objects.create(motobike=model)
        return motobike
        





# Serializer пользователей
class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=("name","phone",)




#Serializers запчастей
class SparePartsSerializers(serializers.ModelSerializer):
    spareparts_country=serializers.CharField(source="country.name")
    class Meta:
        model=SpareParts
        fields=("id","name","state","spareparts_country","code","model","description")