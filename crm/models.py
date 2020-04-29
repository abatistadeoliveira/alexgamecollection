from django.db import models
from django.utils import timezone


# Create your models here.
class Collector(models.Model):
    coll_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    account_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.coll_name)


class Console(models.Model):
    coll_name = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='consoles')
    console_name = models.CharField(max_length=100)
    description = models.TextField()
    console_model = models.CharField(max_length=100)
    console_color = models.CharField(max_length=100)
    console_brand = models.CharField(max_length=100)
    console_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.coll_name)


class VideoGame(models.Model):
    coll_name = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='videogames')
    videogame_name = models.CharField(max_length=100)
    videogame_console = models.CharField(max_length=100)
    v_description = models.TextField()
    quantity = models.IntegerField()
    videogame_charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.coll_name)