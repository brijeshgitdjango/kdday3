from django.db import models

TYPE_CHOICES = (
    ('ac','AC'),
    ('non-ac', 'NON-AC'),
    
)

class Floor(models.Model):
	floorno = models.CharField(max_length=5, unique=True)

	class Meta:
		ordering = ['floorno']

	def __str__(self):
		return self.floorno

class Room(models.Model):
	floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
	room_type = models.CharField(max_length=20 , choices=TYPE_CHOICES, default="non-ac")
	roomno = models.CharField(max_length=5, unique=True)
	fully_allocated = models.BooleanField(default=False)

	class Meta:
		ordering = ['room_type','roomno']
	

	def __str__(self):
		return self.roomno 

class Bed(models.Model):

	room = models.OneToOneField(Room, on_delete=models.CASCADE)
	allocated_count = models.IntegerField(default=0)
	A = models.BooleanField(default=False)
	a_allocated_to = models.CharField(max_length=10, null=True, blank=True)
	B = models.BooleanField(default=False)
	b_allocated_to = models.CharField(max_length=10, null=True, blank=True)
	C = models.BooleanField(default=False)
	c_allocated_to = models.CharField(max_length=10, null=True, blank=True)
	D = models.BooleanField(default=False)
	d_allocated_to = models.CharField(max_length=10, null=True, blank=True)
