from django.db import models
from decimal import Decimal
from phonenumber_field.modelfields import PhoneNumberField
# cars models
class CarsBrand(models.Model):
    name=models.CharField(max_length=30,unique=True,verbose_name="Марка авто")

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name="Марка авто"
        verbose_name_plural="Марки авто"

    



class CarsModel(models.Model):
    brand=models.ForeignKey(CarsBrand,on_delete=models.CASCADE,verbose_name="Марка авто")
    model=models.CharField(max_length=30,verbose_name="Модель авто")

    def __str__(self) -> str:
        return f"{self.brand.name} {self.model}"
    
    class Meta:
        verbose_name="Модель авто"
        verbose_name_plural="Моддели авто"




class CarsColors(models.Model):
    color=models.CharField(max_length=30,verbose_name="Цвет авто")


    def __str__(self) -> str:
        return self.color
    
    class Meta:
        verbose_name="Цвет авто"
        verbose_name_plural="Цвета авто"





class Country(models.Model):
    name=models.CharField(max_length=40,verbose_name="Страна")


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name="Страна"
        verbose_name_plural="Страны"





class Cars(models.Model):
    KPP_CHOICES=(
        ("akpp","Автомат"),
        ("kpp","Механика"),
        ("tiptronic","Типтроник"),
        ("variator","Вариатор"),
        ("robot","Робот")
    )

    WD_CHOICES=(
        ("FWD","Передний"),
        ("RWD","Задний"),
        ("4WD","4WD"),
        ("AWD","Полный")
    )

    STEERING_WEEL_CHOICES=(
        ("right","Спарва"),
        ("left","Слева")
    )

    CARCASE_CHOICES = (
        ('sedan', 'Седан'),
        ('limousine', 'Лимузин'),
        ('pickup', 'Пикап'),
        ('hatchback', 'Хэтчбек'),
        ('wagon', 'Универсал'),
        ('liftback', 'Лифтбек'),
        ('minivan', 'Минивэн'),
        ('coupe', 'Купе'),
        ('cabriolet', 'Кабриолет'),
        ('roadster', 'Родстер'),
        ('targa', 'Тарга')
    )

    FUEL_CHOICES=(
        ("petrol","Бензин"),
        ("gas","Газ"),
        ("diesel","Дизель"),
        ("hybrid","Гибрид"),
        ("electro","Электро")
    )

    STATE_CHOICES = (
        ('B/U', 'Б/У'),
        ('new', 'Новый'),
        ('good', 'Хорошее'),
        ('ideal', 'Идеальное'),
        ('for_parts', 'На запчасти'),
        ('accident', 'Аварийный'),
        ('crashed', 'Битый'),
        ('repainted', 'Крашенный')
    )


    VIN_CHOICES=(
        ("vin_code","Есть VIN код"),
        ("not_vin_code","Без VIN код")
    )




    CURRENCY_CHOICES=(
        ("USD","Доллар"),
        ("KGS","Сом")
    )


    VEHICLE_TYPE_CHOICES = (
        ('car', 'Легковые'),
        ('bus', 'Автобусы'),
        ('truck', 'Грузовики'),
        ('rental', 'Аренда'),
        ('commercial', 'Коммерческая'),
        ('special', 'Спецтехника'),
    )



    cars=models.ForeignKey(CarsModel,on_delete=models.PROTECT,verbose_name="Авто")
    date=models.DateTimeField(auto_now_add=True,verbose_name="Дата пгубликации")
    year = models.IntegerField(choices=[(year, str(year)) for year in range(1900, 2100)],default=2023, verbose_name='Год выпуска')
    currency=models.CharField(max_length=20,choices=CURRENCY_CHOICES,verbose_name="Валюта")
    price=models.BigIntegerField(verbose_name="Цена",default=0)
    mileage=models.BigIntegerField(verbose_name="Пробег",default=1000)
    colors=models.ForeignKey(CarsColors,on_delete=models.PROTECT,verbose_name="Цвет")
    kpp=models.CharField(max_length=30,choices=KPP_CHOICES,verbose_name="КПП")
    wd=models.CharField(max_length=30,choices=WD_CHOICES,verbose_name="Привод")
    steering_weel=models.CharField(max_length=30,choices=STEERING_WEEL_CHOICES,verbose_name="Руль")
    vehicle_type=models.CharField(max_length=20,choices=VEHICLE_TYPE_CHOICES,verbose_name="Тип транспорта")
    carcase=models.CharField(max_length=20,choices=CARCASE_CHOICES,verbose_name="Тип кузова")
    fuel=models.CharField(max_length=20,choices=FUEL_CHOICES,verbose_name="Топливо")
    state=models.CharField(max_length=20,choices=STATE_CHOICES,verbose_name="Состояние")
    vin=models.CharField(max_length=20,choices=VIN_CHOICES,verbose_name="VIN")
    engine_volumes = models.DecimalField(max_digits=3, decimal_places=1, default=0.5,choices=[(Decimal(str(v)), "{:.1f}".format(v)) for v in [i * 0.1 for i in range(5, 101)]],verbose_name='Объем двигателя')
    country=models.ForeignKey(Country,on_delete=models.PROTECT,verbose_name="Страна авто")
    description=models.TextField(verbose_name="Описание")



    def __str__(self) -> str:
        return f"{self.cars}"
    


    class Meta:
        verbose_name="Автомобиль"
        verbose_name_plural="Автомобили"







#motobike model
class MotorbikeBrand(models.Model):
    name=models.CharField(max_length=30,verbose_name="Марка мотоцикла")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name="Марка мотоцикла"
        verbose_name_plural="Марки мотоциклов"




class MotobikeModel(models.Model):
    brand=models.ForeignKey(MotorbikeBrand,on_delete=models.PROTECT,verbose_name="Марка мотоцикла")
    model=models.CharField(max_length=30,verbose_name="Модель мотоцикла")

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"
    

    class Meta:
        verbose_name="Модель мотоцикла"
        verbose_name_plural="Модели мотоциклов"



class Motobike(models.Model):


    STATE_CHOICES = (
        ('B/U', 'Б/У'),
        ('new', 'Новый'),
        ('good', 'Хорошее'),
        ('ideal', 'Идеальное'),
        ('for_parts', 'На запчасти'),
        ('accident', 'Аварийный'),
        ('crashed', 'Битый'),
        ('repainted', 'Крашенный')
    )
    

    ENGINE_CHOICES=(
        ("2 stroke","2х тактный"),
        ("4 stroke","4х тактный")
    )



    ENGINE_VOLUMES_CHOICES = (
     ("50см³", "50куб"), 
     ("100см³", "100куб"),
     ("125см³", "125куб"),
     ("150см³", "150куб"),
     ("200см³", "200куб"),
     ("250см³", "250куб"),  
     ("350см³", "350куб"),
     ("500см³", "500куб"),
     ("600см³", "600куб"), 
     ("750см³", "750куб"),
     ("1000см³", "1000куб"),
     ("1200см³", "1200куб"),
     ("1800см³", "1800куб")
)




    FUEL_CHOICES=(
        ("petrol","Бензин"),
        ("electro","Электро")
    )


    CLASS_CHOICES=(
        ("classical","Класический"),
        ("tourist","Туристический"),
        ("sport","Спортивный"),
        ("chopper","Чоппер"),
        ("enduro","Эндуро"),
        ("cross","Кроссовый")
    )



    KPP_CHOICES=(
        ("akpp","Автомат"),
        ("kpp","Механика")
    )



    motobike=models.ForeignKey(MotobikeModel,on_delete=models.PROTECT,verbose_name="Мотоцикл")
    date=models.DateTimeField(auto_now_add=True,verbose_name="Дата публикации")
    year = models.IntegerField(choices=[(year, str(year)) for year in range(1900, 2100)],default=2023, verbose_name='Год выпуска')
    engine_volumes = models.CharField(max_length=20,choices=ENGINE_VOLUMES_CHOICES,verbose_name="Объем двигателя")
    mileage=models.BigIntegerField(verbose_name="Пробег",default=12345678)
    state=models.CharField(max_length=20,choices=STATE_CHOICES,verbose_name="Состояние")
    price=models.IntegerField(verbose_name="Цена",default=1000000)
    engine=models.CharField(max_length=10,choices=ENGINE_CHOICES,verbose_name="Двигатель")
    fuel=models.CharField(max_length=20,choices=FUEL_CHOICES,verbose_name="Топливо")
    country=models.ForeignKey(Country,on_delete=models.PROTECT,verbose_name="Страна")
    class_moto=models.CharField(max_length=20,choices=CLASS_CHOICES,verbose_name="Класс")


    def __str__(self) -> str:
        return f"{self.motobike}"
    

    class Meta:
        verbose_name="Мотоцикл"
        verbose_name_plural="Мотоциклы"





#user model
class Users(models.Model):
    name=models.CharField(max_length=30,verbose_name="Имя")
    phone=PhoneNumberField(max_length=20,region="KG",verbose_name="Номер телефона+996")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"







class SpareParts(models.Model):
    STATE_CHOICES = (
        ('B/U', 'Б/У'),
        ('new', 'Новый')
    )

    name = models.CharField(max_length=50, verbose_name="Название")
    state = models.CharField(max_length=10, choices=STATE_CHOICES, verbose_name="Состояние")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name="Страна")
    code = models.CharField(max_length=50, unique=True, verbose_name="Код запчасти")
    model = models.ManyToManyField(CarsModel, verbose_name="Для моделей")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name="Запчасть"
        verbose_name_plural="Запчасти"
