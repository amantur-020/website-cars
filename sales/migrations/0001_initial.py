# Generated by Django 3.2 on 2023-08-07 16:22

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Марка авто')),
            ],
            options={
                'verbose_name': 'Марка авто',
                'verbose_name_plural': 'Марки авто',
            },
        ),
        migrations.CreateModel(
            name='CarsColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30, verbose_name='Цвет авто')),
            ],
            options={
                'verbose_name': 'Цвет авто',
                'verbose_name_plural': 'Цвета авто',
            },
        ),
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, verbose_name='Модель авто')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.carsbrand', verbose_name='Марка авто')),
            ],
            options={
                'verbose_name': 'Модель авто',
                'verbose_name_plural': 'Моддели авто',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='MotorbikeBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Марка мотоцикла')),
            ],
            options={
                'verbose_name': 'Марка мотоцикла',
                'verbose_name_plural': 'Марки мотоциклов',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region='KG', verbose_name='Номер телефона+996')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='SpareParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('state', models.CharField(choices=[('B/U', 'Б/У'), ('new', 'Новый')], max_length=10, verbose_name='Состояние')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Код запчасти')),
                ('description', models.TextField(verbose_name='Описание')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.country', verbose_name='Страна')),
                ('model', models.ManyToManyField(to='sales.CarsModel', verbose_name='Для моделей')),
            ],
            options={
                'verbose_name': 'Запчасть',
                'verbose_name_plural': 'Запчасти',
            },
        ),
        migrations.CreateModel(
            name='MotobikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, verbose_name='Модель мотоцикла')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.motorbikebrand', verbose_name='Марка мотоцикла')),
            ],
            options={
                'verbose_name': 'Модель мотоцикла',
                'verbose_name_plural': 'Модели мотоциклов',
            },
        ),
        migrations.CreateModel(
            name='Motobike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('year', models.IntegerField(choices=[(1900, '1900'), (1901, '1901'), (1902, '1902'), (1903, '1903'), (1904, '1904'), (1905, '1905'), (1906, '1906'), (1907, '1907'), (1908, '1908'), (1909, '1909'), (1910, '1910'), (1911, '1911'), (1912, '1912'), (1913, '1913'), (1914, '1914'), (1915, '1915'), (1916, '1916'), (1917, '1917'), (1918, '1918'), (1919, '1919'), (1920, '1920'), (1921, '1921'), (1922, '1922'), (1923, '1923'), (1924, '1924'), (1925, '1925'), (1926, '1926'), (1927, '1927'), (1928, '1928'), (1929, '1929'), (1930, '1930'), (1931, '1931'), (1932, '1932'), (1933, '1933'), (1934, '1934'), (1935, '1935'), (1936, '1936'), (1937, '1937'), (1938, '1938'), (1939, '1939'), (1940, '1940'), (1941, '1941'), (1942, '1942'), (1943, '1943'), (1944, '1944'), (1945, '1945'), (1946, '1946'), (1947, '1947'), (1948, '1948'), (1949, '1949'), (1950, '1950'), (1951, '1951'), (1952, '1952'), (1953, '1953'), (1954, '1954'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027'), (2028, '2028'), (2029, '2029'), (2030, '2030'), (2031, '2031'), (2032, '2032'), (2033, '2033'), (2034, '2034'), (2035, '2035'), (2036, '2036'), (2037, '2037'), (2038, '2038'), (2039, '2039'), (2040, '2040'), (2041, '2041'), (2042, '2042'), (2043, '2043'), (2044, '2044'), (2045, '2045'), (2046, '2046'), (2047, '2047'), (2048, '2048'), (2049, '2049'), (2050, '2050'), (2051, '2051'), (2052, '2052'), (2053, '2053'), (2054, '2054'), (2055, '2055'), (2056, '2056'), (2057, '2057'), (2058, '2058'), (2059, '2059'), (2060, '2060'), (2061, '2061'), (2062, '2062'), (2063, '2063'), (2064, '2064'), (2065, '2065'), (2066, '2066'), (2067, '2067'), (2068, '2068'), (2069, '2069'), (2070, '2070'), (2071, '2071'), (2072, '2072'), (2073, '2073'), (2074, '2074'), (2075, '2075'), (2076, '2076'), (2077, '2077'), (2078, '2078'), (2079, '2079'), (2080, '2080'), (2081, '2081'), (2082, '2082'), (2083, '2083'), (2084, '2084'), (2085, '2085'), (2086, '2086'), (2087, '2087'), (2088, '2088'), (2089, '2089'), (2090, '2090'), (2091, '2091'), (2092, '2092'), (2093, '2093'), (2094, '2094'), (2095, '2095'), (2096, '2096'), (2097, '2097'), (2098, '2098'), (2099, '2099')], default=2023, verbose_name='Год выпуска')),
                ('engine_volumes', models.CharField(choices=[('50см³', '50куб'), ('100см³', '100куб'), ('125см³', '125куб'), ('150см³', '150куб'), ('200см³', '200куб'), ('250см³', '250куб'), ('350см³', '350куб'), ('500см³', '500куб'), ('600см³', '600куб'), ('750см³', '750куб'), ('1000см³', '1000куб'), ('1200см³', '1200куб'), ('1800см³', '1800куб')], max_length=20, verbose_name='Объем двигателя')),
                ('mileage', models.BigIntegerField(default=12345678, verbose_name='Пробег')),
                ('state', models.CharField(choices=[('B/U', 'Б/У'), ('new', 'Новый'), ('good', 'Хорошее'), ('ideal', 'Идеальное'), ('for_parts', 'На запчасти'), ('accident', 'Аварийный'), ('crashed', 'Битый'), ('repainted', 'Крашенный')], max_length=20, verbose_name='Состояние')),
                ('price', models.IntegerField(default=1000000, verbose_name='Цена')),
                ('engine', models.CharField(choices=[('2 stroke', '2х тактный'), ('4 stroke', '4х тактный')], max_length=10, verbose_name='Двигатель')),
                ('fuel', models.CharField(choices=[('petrol', 'Бензин'), ('electro', 'Электро')], max_length=20, verbose_name='Топливо')),
                ('class_moto', models.CharField(choices=[('classical', 'Класический'), ('tourist', 'Туристический'), ('sport', 'Спортивный'), ('chopper', 'Чоппер'), ('enduro', 'Эндуро'), ('cross', 'Кроссовый')], max_length=20, verbose_name='Класс')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.country', verbose_name='Страна')),
                ('motobike', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.motobikemodel', verbose_name='Мотоцикл')),
            ],
            options={
                'verbose_name': 'Мотоцикл',
                'verbose_name_plural': 'Мотоциклы',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата пгубликации')),
                ('year', models.IntegerField(choices=[(1900, '1900'), (1901, '1901'), (1902, '1902'), (1903, '1903'), (1904, '1904'), (1905, '1905'), (1906, '1906'), (1907, '1907'), (1908, '1908'), (1909, '1909'), (1910, '1910'), (1911, '1911'), (1912, '1912'), (1913, '1913'), (1914, '1914'), (1915, '1915'), (1916, '1916'), (1917, '1917'), (1918, '1918'), (1919, '1919'), (1920, '1920'), (1921, '1921'), (1922, '1922'), (1923, '1923'), (1924, '1924'), (1925, '1925'), (1926, '1926'), (1927, '1927'), (1928, '1928'), (1929, '1929'), (1930, '1930'), (1931, '1931'), (1932, '1932'), (1933, '1933'), (1934, '1934'), (1935, '1935'), (1936, '1936'), (1937, '1937'), (1938, '1938'), (1939, '1939'), (1940, '1940'), (1941, '1941'), (1942, '1942'), (1943, '1943'), (1944, '1944'), (1945, '1945'), (1946, '1946'), (1947, '1947'), (1948, '1948'), (1949, '1949'), (1950, '1950'), (1951, '1951'), (1952, '1952'), (1953, '1953'), (1954, '1954'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027'), (2028, '2028'), (2029, '2029'), (2030, '2030'), (2031, '2031'), (2032, '2032'), (2033, '2033'), (2034, '2034'), (2035, '2035'), (2036, '2036'), (2037, '2037'), (2038, '2038'), (2039, '2039'), (2040, '2040'), (2041, '2041'), (2042, '2042'), (2043, '2043'), (2044, '2044'), (2045, '2045'), (2046, '2046'), (2047, '2047'), (2048, '2048'), (2049, '2049'), (2050, '2050'), (2051, '2051'), (2052, '2052'), (2053, '2053'), (2054, '2054'), (2055, '2055'), (2056, '2056'), (2057, '2057'), (2058, '2058'), (2059, '2059'), (2060, '2060'), (2061, '2061'), (2062, '2062'), (2063, '2063'), (2064, '2064'), (2065, '2065'), (2066, '2066'), (2067, '2067'), (2068, '2068'), (2069, '2069'), (2070, '2070'), (2071, '2071'), (2072, '2072'), (2073, '2073'), (2074, '2074'), (2075, '2075'), (2076, '2076'), (2077, '2077'), (2078, '2078'), (2079, '2079'), (2080, '2080'), (2081, '2081'), (2082, '2082'), (2083, '2083'), (2084, '2084'), (2085, '2085'), (2086, '2086'), (2087, '2087'), (2088, '2088'), (2089, '2089'), (2090, '2090'), (2091, '2091'), (2092, '2092'), (2093, '2093'), (2094, '2094'), (2095, '2095'), (2096, '2096'), (2097, '2097'), (2098, '2098'), (2099, '2099')], default=2023, verbose_name='Год выпуска')),
                ('currency', models.CharField(choices=[('USD', 'Доллар'), ('KGS', 'Сом')], max_length=20, verbose_name='Валюта')),
                ('price', models.BigIntegerField(default=0, verbose_name='Цена')),
                ('mileage', models.BigIntegerField(default=1000, verbose_name='Пробег')),
                ('kpp', models.CharField(choices=[('akpp', 'Автомат'), ('kpp', 'Механика'), ('tiptronic', 'Типтроник'), ('variator', 'Вариатор'), ('robot', 'Робот')], max_length=30, verbose_name='КПП')),
                ('wd', models.CharField(choices=[('FWD', 'Передний'), ('RWD', 'Задний'), ('4WD', '4WD'), ('AWD', 'Полный')], max_length=30, verbose_name='Привод')),
                ('steering_weel', models.CharField(choices=[('right', 'Спарва'), ('left', 'Слева')], max_length=30, verbose_name='Руль')),
                ('vehicle_type', models.CharField(choices=[('car', 'Легковые'), ('bus', 'Автобусы'), ('truck', 'Грузовики'), ('rental', 'Аренда'), ('commercial', 'Коммерческая'), ('special', 'Спецтехника')], max_length=20, verbose_name='Тип транспорта')),
                ('carcase', models.CharField(choices=[('sedan', 'Седан'), ('limousine', 'Лимузин'), ('pickup', 'Пикап'), ('hatchback', 'Хэтчбек'), ('wagon', 'Универсал'), ('liftback', 'Лифтбек'), ('minivan', 'Минивэн'), ('coupe', 'Купе'), ('cabriolet', 'Кабриолет'), ('roadster', 'Родстер'), ('targa', 'Тарга')], max_length=20, verbose_name='Тип кузова')),
                ('fuel', models.CharField(choices=[('petrol', 'Бензин'), ('gas', 'Газ'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electro', 'Электро')], max_length=20, verbose_name='Топливо')),
                ('state', models.CharField(choices=[('B/U', 'Б/У'), ('new', 'Новый'), ('good', 'Хорошее'), ('ideal', 'Идеальное'), ('for_parts', 'На запчасти'), ('accident', 'Аварийный'), ('crashed', 'Битый'), ('repainted', 'Крашенный')], max_length=20, verbose_name='Состояние')),
                ('vin', models.CharField(choices=[('vin_code', 'Есть VIN код'), ('not_vin_code', 'Без VIN код')], max_length=20, verbose_name='VIN')),
                ('engine_volumes', models.DecimalField(choices=[(Decimal('0.5'), '0.5'), (Decimal('0.6000000000000001'), '0.6'), (Decimal('0.7000000000000001'), '0.7'), (Decimal('0.8'), '0.8'), (Decimal('0.9'), '0.9'), (Decimal('1.0'), '1.0'), (Decimal('1.1'), '1.1'), (Decimal('1.2000000000000002'), '1.2'), (Decimal('1.3'), '1.3'), (Decimal('1.4000000000000001'), '1.4'), (Decimal('1.5'), '1.5'), (Decimal('1.6'), '1.6'), (Decimal('1.7000000000000002'), '1.7'), (Decimal('1.8'), '1.8'), (Decimal('1.9000000000000001'), '1.9'), (Decimal('2.0'), '2.0'), (Decimal('2.1'), '2.1'), (Decimal('2.2'), '2.2'), (Decimal('2.3000000000000003'), '2.3'), (Decimal('2.4000000000000004'), '2.4'), (Decimal('2.5'), '2.5'), (Decimal('2.6'), '2.6'), (Decimal('2.7'), '2.7'), (Decimal('2.8000000000000003'), '2.8'), (Decimal('2.9000000000000004'), '2.9'), (Decimal('3.0'), '3.0'), (Decimal('3.1'), '3.1'), (Decimal('3.2'), '3.2'), (Decimal('3.3000000000000003'), '3.3'), (Decimal('3.4000000000000004'), '3.4'), (Decimal('3.5'), '3.5'), (Decimal('3.6'), '3.6'), (Decimal('3.7'), '3.7'), (Decimal('3.8000000000000003'), '3.8'), (Decimal('3.9000000000000004'), '3.9'), (Decimal('4.0'), '4.0'), (Decimal('4.1000000000000005'), '4.1'), (Decimal('4.2'), '4.2'), (Decimal('4.3'), '4.3'), (Decimal('4.4'), '4.4'), (Decimal('4.5'), '4.5'), (Decimal('4.6000000000000005'), '4.6'), (Decimal('4.7'), '4.7'), (Decimal('4.800000000000001'), '4.8'), (Decimal('4.9'), '4.9'), (Decimal('5.0'), '5.0'), (Decimal('5.1000000000000005'), '5.1'), (Decimal('5.2'), '5.2'), (Decimal('5.300000000000001'), '5.3'), (Decimal('5.4'), '5.4'), (Decimal('5.5'), '5.5'), (Decimal('5.6000000000000005'), '5.6'), (Decimal('5.7'), '5.7'), (Decimal('5.800000000000001'), '5.8'), (Decimal('5.9'), '5.9'), (Decimal('6.0'), '6.0'), (Decimal('6.1000000000000005'), '6.1'), (Decimal('6.2'), '6.2'), (Decimal('6.300000000000001'), '6.3'), (Decimal('6.4'), '6.4'), (Decimal('6.5'), '6.5'), (Decimal('6.6000000000000005'), '6.6'), (Decimal('6.7'), '6.7'), (Decimal('6.800000000000001'), '6.8'), (Decimal('6.9'), '6.9'), (Decimal('7.0'), '7.0'), (Decimal('7.1000000000000005'), '7.1'), (Decimal('7.2'), '7.2'), (Decimal('7.300000000000001'), '7.3'), (Decimal('7.4'), '7.4'), (Decimal('7.5'), '7.5'), (Decimal('7.6000000000000005'), '7.6'), (Decimal('7.7'), '7.7'), (Decimal('7.800000000000001'), '7.8'), (Decimal('7.9'), '7.9'), (Decimal('8.0'), '8.0'), (Decimal('8.1'), '8.1'), (Decimal('8.200000000000001'), '8.2'), (Decimal('8.3'), '8.3'), (Decimal('8.4'), '8.4'), (Decimal('8.5'), '8.5'), (Decimal('8.6'), '8.6'), (Decimal('8.700000000000001'), '8.7'), (Decimal('8.8'), '8.8'), (Decimal('8.9'), '8.9'), (Decimal('9.0'), '9.0'), (Decimal('9.1'), '9.1'), (Decimal('9.200000000000001'), '9.2'), (Decimal('9.3'), '9.3'), (Decimal('9.4'), '9.4'), (Decimal('9.5'), '9.5'), (Decimal('9.600000000000001'), '9.6'), (Decimal('9.700000000000001'), '9.7'), (Decimal('9.8'), '9.8'), (Decimal('9.9'), '9.9'), (Decimal('10.0'), '10.0')], decimal_places=1, default=0.5, max_digits=3, verbose_name='Объем двигателя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.carsmodel', verbose_name='Авто')),
                ('colors', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.carscolors', verbose_name='Цвет')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.country', verbose_name='Страна авто')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
