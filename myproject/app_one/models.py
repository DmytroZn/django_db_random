from django.db import models

# Create your models here.

from multiselectfield import MultiSelectField


# class Agregat(models.Model):
#     n_zag = models.CharField(verbose_name='гос номер', max_length=40, blank=True)
#     n_agr = models.IntegerField(verbose_name='номер агрегата')
#     n_zone = models.IntegerField()
#     corpus = models.ForeignKey('Corpus', on_delete=models.CASCADE)
#     # n_zone = models.ForeignKey('Zone', on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{str(self.n_agr)} - {self.n_zag}'
class Agregat(models.Model):
    n_zag = models.CharField(verbose_name='гос номер', max_length=40, blank=True)
    n_agr = models.IntegerField(verbose_name='номер агрегата')
    # n_zone = models.IntegerField()
    # corpus = models.ForeignKey('Corpus', on_delete=models.CASCADE)
    n_zone = models.ForeignKey('Zone', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.n_zone} Агрегат - {str(self.n_agr)};'



class Zone(models.Model):
    n_zone = models.IntegerField(verbose_name='номер зони')
    corpus = models.ForeignKey('Corpus', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.corpus} Зона - {str(self.n_zone)};'

class Corpus(models.Model):
    name_corpus = models.IntegerField(unique=True)
    def __str__(self):
        return f'Корпус - {str(self.name_corpus)};'


# class CorpProducts(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class ZonPizza(models.Model):
#     fat = models.CharField(max_length=50)
#     products = models.ManyToManyField(CorpProducts)
#     def __str__(self):
#         return self.fat

# class AgrDom(models.Model):
#     name = models.CharField(max_length=50)
#     # zon = models.ManyToManyField(ZonPizza)
#     one = models.OneToOneField(ZonPizza, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class Zones(models.Model):
#     AGREG = (
#         ('1 agr', '1 agr'),
#         ('2 agr', '2 agr'),
#         ('3 agr', '3 agr'),
#         ('4 agr', '4 agr'),
#         ('5 agr', '5 agr'),
#         ('6 agr', '6 agr'),
#         ('7 agr', '7 agr'),
#         ('8 agr', '8 agr'),

#     )
    
#     one_zone = MultiSelectField(choices=AGREG, blank=True)
#     two_zone = MultiSelectField(choices=AGREG, blank=False)
#     three_zone = MultiSelectField(choices=AGREG)
#     four_zone = MultiSelectField(choices=AGREG)
#     five_zone = MultiSelectField(choices=AGREG)
#     six_zone = MultiSelectField(choices=AGREG)
#     seven_zone = MultiSelectField(choices=AGREG)
#     eight_zone = MultiSelectField(choices=AGREG)
    

# class Corpuses(models.Model):
#     ZONES = (
#         ('2 zona', '2 zona'),
#         ('1 zona', '1 zona'),
#         ('3 zona', '3 zona'),
#         ('4 zona', '4 zona'),
#         ('5 zona', '5 zona'),
#         ('6 zona', '6 zona'),
#         ('7 zona', '7 zona'),
#         ('8 zona', '8 zona'),

#     )
#     number_corpus = models.IntegerField(unique=True)
#     include_zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
#     zones = MultiSelectField(choices=ZONES, blank=True)




class Agregate(models.Model):
    number_of_controller = models.IntegerField(verbose_name='№ Контролдлера', null=True)
    t_delta = models.IntegerField(verbose_name='T дельта', null=True)
    t_input = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Температура входу', null=True)
    t_output = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Температура виходу', null=True)
    auto_hand = models.CharField(max_length=30, null=True)
    capacity = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Обєм', null=True)
    capacity_warm = models.DecimalField(max_digits=1000, decimal_places=2, verbose_name='Обєм тепла', null=True)
    capacity_current = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Обєм поточний', null=True)
    pressure = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Тиск виходу', null=True)
    digital_input = models.IntegerField(verbose_name='Цифровий вхід', null=True)
    digital_output = models.IntegerField(verbose_name='Цифровий вихід', null=True)
    parameters = models.IntegerField(verbose_name='T дельта', null=True)
    w_accumulate = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='W накоп.', null=True)
    w_current = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='W пот.', null=True)
    zdate = models.DateField(verbose_name="Дата зони", null=True)
    ztime = models.TimeField(verbose_name="Час зони", null=True)

class MaAgregate(models.Model):
    number_of_controller = models.IntegerField(blank=True, null=True)
    t_delta = models.IntegerField(blank=True, null=True)
    t_input = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    t_output = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    auto_hand = models.CharField(max_length=30, blank=True, null=True)
    capacity = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    capacity_warm = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True)
    capacity_current = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    pressure = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    digital_input = models.IntegerField(blank=True, null=True)
    digital_output = models.IntegerField(blank=True, null=True)
    parameters = models.IntegerField(blank=True, null=True)
    w_accumulate = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    w_current = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    zdate = models.DateField(blank=True, null=True)
    ztime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_agregate'