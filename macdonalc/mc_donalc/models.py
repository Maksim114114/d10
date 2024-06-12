from datetime import datetime

from django.db import models
#from .resources import POSITIONS,cashier
from mc_donalc.resources import POSITIONS,cashier




class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)#datetime, который позволяет получить текущее время
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)

    products = models.ManyToManyField("Product", through='ProductOrder')#МНОГИМ КО МНОГИМ

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()



#еще один метод ордера   считать время выполния заказа
    def get_duration(self):#duration-продолжтьельность
        if self.complete:
            return (self.time_out - self.time_in).total_seconds()
        else:
            return (datetime.now() - self.time_in).total_seconds()




class Product(models.Model):# // здесь будут определения полей
    name = models.CharField(max_length=255)#поле 2 name тип CHAR(255)
    price = models.FloatField(default=0.0)
    composition = models.TextField(default="Состав не указан")


class Product1(models.Model):# // здесь будут определения полей
    name = models.CharField(max_length=255)#поле 2 name тип CHAR(255)
    price = models.FloatField(default=0.0)
    composition = models.TextField(default="Состав не указан")





class Staff(models.Model):
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'


    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2,choices=POSITIONS,default=cashier)
    labor_contract = models.IntegerField()


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True)
    email = models.CharField(max_length=255)




class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    _amount = models.IntegerField(default=1,db_column='amount')
#метод возвращает полную сумму
    def product_summ(self):#посчитать полную сумму этого продукта в заказе
        return self.product.price * self.amount
#ДЕКАРАТОР
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()









# Create your models here.
