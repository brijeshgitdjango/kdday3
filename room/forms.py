from django import forms
from .models import Floor, Room

class FloorForm(forms.ModelForm):
	floorno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Floor No.'}))
	class Meta:
		model=Floor
		fields=['floorno']


class RoomForm(forms.ModelForm):
	roomno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Room No.'}))
	class Meta:
		model=Room
		fields = ['floor', 'roomno', 'room_type']