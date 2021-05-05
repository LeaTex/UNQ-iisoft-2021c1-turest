from django.db import models
from django.utils import timezone

class Item(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
