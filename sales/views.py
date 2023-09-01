from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import filters
from .models import *
from .serializers import *
import django_filters
from rest_framework import viewsets
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from rest_framework.response import Response


# функция главной страницы
def main_page(request):
    return render(request,'html/index.html')



# View машины
class CarsViewset(viewsets.ModelViewSet):
    queryset=Cars.objects.all()
    serializer_class=CarsSerializers
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields=("cars__brand__name","date","year","price","colors__color",
                      "kpp","wd","steering_weel","vehicle_type","carcase",
                      "fuel","state","vin","engine_volumes","country",)


class NewAnnouncementslistAPIView(ListAPIView):
    serializer_class=CarsSerializers

    def get_queryset(self):
        new_announcements=timezone.now()-timedelta(weeks=1)
        return Cars.objects.filter(date__gte=new_announcements)


class NewCarslistAPIView(ListAPIView):
    serializer_class=CarsSerializers

    def get_queryset(self):
        return Cars.objects.filter(year__gte=2021)
    

class AllCarsBrandAPIView(ListAPIView):
    serializer_class=CarsBrandSerializers

    def get_queryset(self):
        return CarsBrand.objects.all()
    


class AllCountryAPIView(ListAPIView):
    serializer_class=CarsCountrySerializers

    def get_queryset(self):
        return Country.objects.all()
    




# View мотоцикла
class MotobikeViewset(viewsets.ModelViewSet):
    queryset=Motobike.objects.all()
    serializer_class=MotobikeSerializers
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields=("motobike__brand__name","date","year","engine_volumes",
                "mileage","state","price","engine","fuel","class_moto")
    
    def get_queryset(self):
        return Motobike.objects.all()
    


class AllMotobikeAPIView(ListAPIView):
    serializer_class=MotobikeSerializers
    queryset=Motobike.objects.all()
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields=("motobike__brand__name","date","year","engine_volumes",
                "mileage","state","price","engine","fuel","class_moto")
    
    






class AllMotobikeBrandAPIView(ListAPIView):
    serializer_class=MotobikeBramdSerializers

    def get_queryset(self):

        return MotorbikeBrand.objects.all()




#View пользователей
class UserslistAPIView(ListAPIView):
    serializer_class=UsersSerializers

    def get_queryset(self):
        return Users.objects.all()



#View Запчастей
class SparePartsViewset(viewsets.ModelViewSet):
    queryset=SpareParts.objects.all()
    serializer_class=SparePartsSerializers
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields=("name","state","country__name","code","model")
