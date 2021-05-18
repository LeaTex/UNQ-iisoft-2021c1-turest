from django.db import models
from django.utils import timezone

class Item(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    updateDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updateDate = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Mozo(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    telefono = models.PositiveIntegerField()
    mail = models.EmailField(max_length=200)

    def publish(self):
        self.updateDate = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
