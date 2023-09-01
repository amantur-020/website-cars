from django.urls import path
from .views import *

urlpatterns=[
    #cars
    path("",main_page,name="main_page"),
    path("cars/",CarsViewset.as_view(
        {
            "get":"list",
            "post":"create",
            "put":"update",
            "patch":"partial_update",
            "delete":"destroy"
        }
    )),
    path("new_auto/",NewCarslistAPIView.as_view()),
    path("all_cars_brand/",AllCarsBrandAPIView.as_view()),
    path("all_cars_contry/",AllCountryAPIView.as_view()),
    path("new_announcements/",NewAnnouncementslistAPIView.as_view()),

    #users
    path("users/",UserslistAPIView.as_view()),


    #motobike
    path("motobike/",MotobikeViewset.as_view(
        {
            "get":"list",
            "post":"create",
            "put":"update",
            "patch":"partial_update",
            "delete":"destroy"
        })),
    path("all_motobike_brand/",AllMotobikeBrandAPIView.as_view()),
    path("all_motobike/",AllMotobikeAPIView.as_view()),


    #spareparts
    path("spareparts/",SparePartsViewset.as_view({
            "get":"list",
            "post":"create",
            "put":"update",
            "patch":"partial_update",
            "delete":"destroy"
        }))
]