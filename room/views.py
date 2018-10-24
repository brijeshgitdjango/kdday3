from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Floor, Room, Bed
from .forms import FloorForm, RoomForm

def FloorAddView(request):
	form = FloorForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("room:floor_list"))
	context = {
		'form':form,
		'title':'Floor Add',
		'btn_title':'Submit',
	}
	return render(request, 'room/form.html', context)

def FloorListView(request):
	return render(request, 'room/floor_list.html', {'floor':Floor.objects.all()})

def FloorUpdateView(request, id=None):
	instance = get_object_or_404(Floor, id=id)
	form = FloorForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("room:floor_list"))
	context = {
		'form':form,
		'title':'FloorUpdate',
		'btn_title':'Update',
	}
	return render(request, 'room/form.html', context)

def FloorDeleteView(request, id=None):
	instance = get_object_or_404(Floor, id=id)
	if request.method=="POST":
		instance.delete()
		return HttpResponseRedirect(reverse("room:floor_list"))

	context = {
		'instance':instance,
		'title':'Floor',
		'data':instance.floorno,
	}
	return render(request, 'room/delete.html' ,context)



def RoomAddView(request):
	form = RoomForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			instance = Room(
				floor=form.cleaned_data.get('floor'),
				room_type=form.cleaned_data.get('room_type'),
				roomno=form.cleaned_data.get('roomno'),
				)
			instance.save()
			Bed.objects.create(room_id=instance.id)
			return HttpResponseRedirect(reverse("room:room_list"))
	context = {
		'form':form,
		'title':'Room Add',
		'btn_title':'Submit',
	}
	return render(request, 'room/form.html', context)

def RoomDetailView(request, id=None):
	room_obj = get_object_or_404(Room, id=id)
	instance = get_object_or_404(Bed, room=room_obj)
	beda=None;bedb=None;bedc=None;bedd=None
	if instance.A:
		beda = get_object_or_404(Student, mobile=instance.a_allocated_to)
	if instance.B:
		bedb = get_object_or_404(Student, mobile=instance.b_allocated_to)
	if instance.C:
		bedc = get_object_or_404(Student, mobile=instance.c_allocated_to)
	if instance.D:
		bedd = get_object_or_404(Student, mobile=instance.d_allocated_to)
	context = {
		'room':room_obj,
		'beda':beda,
		'bedb':bedb,
		'bedc':bedc,
		'bedd':bedd,

	}
	return render(request, 'room/room_details.html', context)

def RoomListView(request):
	room = Room.objects.all()
	return render(request, 'room/list.html', {'room':room, 'title':'Room'})


def RoomUpdateView(request, id=None):
	instance = get_object_or_404(Room, id=id)
	form = RoomForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("room:room_list"))
	context = {
		'form':form,
		'title':'RoomUpdate',
		'btn_title':'Update',
	}
	return render(request, 'room/form.html', context)

def RoomDeleteView(request, id=None):
	instance = get_object_or_404(Room, id=id)
	if request.method=="POST":
		instance.delete()
		return HttpResponseRedirect(reverse("room:room_list"))

	context = {
		'instance':instance,
		'title':'Room',
		'data':instance.roomno,
	}
	return render(request, 'room/delete.html' ,context)