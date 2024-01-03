from django.db import models


# class Publisher(models.Model):
#     title = models.CharField(max_length=31, blank=False, verbose_name='نام')


# class Category(models.Model):
#     title = models.CharField(max_length=31, blank=False, verbose_name='نام')


# class Book(models.Model):
#     title = models.CharField(max_length=31, blank=False, verbose_name='نام')
#     create_date = models.DateField(null=True, blank=True, verbose_name='تاریخ ایجاد')
#     last_update = models.DateTimeField(null=True, blank=True)
#     categories = models.ManyToManyField(Category, related_name='books', blank=False)
#     publisher = models.ForeignKey(Publisher, related_name='books', null=True, on_delete=models.SET_NULL)
#     price = models.IntegerField(null=True, blank=True, verbose_name='قیمت')

#     def __str__(self):
#         return f"{self.title} - {self.create_date}"


# در فایل models.py

from django.db import models

class FlightTicket(models.Model):
    # اطلاعات مسافر
    passenger_name = models.CharField(max_length=100, verbose_name='نام مسافر')
    passenger_email = models.EmailField(verbose_name='ایمیل مسافر')

    # اطلاعات پرواز
    departure_city = models.CharField(max_length=100, verbose_name='شهر حرکت')
    destination_city = models.CharField(max_length=100, verbose_name='شهر مقصد')
    departure_date = models.DateField(verbose_name='تاریخ حرکت')
    arrival_date = models.DateField(verbose_name='تاریخ ورود')

    # اطلاعات بلیط
    ticket_number = models.CharField(max_length=20, unique=True, verbose_name='شماره بلیط')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت بلیط')

    # اطلاعات اضافی
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f"{self.passenger_name} - {self.ticket_number}"

    class Meta:
        verbose_name = 'بلیط هواپیما'
        verbose_name_plural = 'بلیط‌های هواپیما'


    # def clean(self):
    #     if self.price > 10000:
    #         super(Book, self).clean()
    #     else:
    #         raise ValidationError('price > 10.000')

    # def save(self, *args, **kwargs):
    #     if self.price < 2000:
    #         raise ValueError('price < 2000')
    #     super(Book, self).save()
