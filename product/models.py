from django.db import models

class FlightDestination(models.Model):
    city = models.CharField(max_length=100, verbose_name='شهر')

    def __str__(self):
        return self.city

class FlightTicket(models.Model):
    passenger_name = models.CharField(max_length=100, verbose_name='نام مسافر')
    passenger_email = models.EmailField(verbose_name='ایمیل مسافر')

    departure_cities = models.ManyToManyField(FlightDestination, related_name='departure_tickets', verbose_name='شهر حرکت')
    destination_cities = models.ManyToManyField(FlightDestination, related_name='destination_tickets', verbose_name='شهر مقصد')

    departure_date = models.DateField(verbose_name='تاریخ حرکت')
    arrival_date = models.DateField(verbose_name='تاریخ ورود')

    ticket_number = models.CharField(max_length=20, unique=True, verbose_name='شماره بلیط')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت بلیط')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f"{self.passenger_name} - {self.ticket_number}"

    class Meta:
        verbose_name = 'بلیط هواپیما'
        verbose_name_plural = 'بلیط‌های هواپیما'
