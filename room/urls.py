from django.conf.urls import url
from .views import (
	FloorAddView,
	FloorListView,
	FloorUpdateView,
	FloorDeleteView,
	RoomAddView,
	RoomDetailView,
	RoomListView,
	RoomUpdateView,
	RoomDeleteView,
	)

urlpatterns = [
    url(r'^floor/$',FloorListView , name="floor_list"),
    url(r'^floor/add/$', FloorAddView, name="floor_add"), 
	url(r'^floor/(?P<id>\d+)/update/$', FloorUpdateView, name='floor_update'),
	url(r'^floor/(?P<id>\d+)/delete/$', FloorDeleteView, name='floor_delete'),
	url(r'^$',RoomListView , name="room_list"),
	url(r'^(?P<id>\d+)/$', RoomDetailView, name='room_detail'),
    url(r'^add/$', RoomAddView, name="room_add"),
    url(r'^(?P<id>\d+)/update/$', RoomUpdateView, name='room_update'),
	url(r'^(?P<id>\d+)/delete/$', RoomDeleteView, name='room_delete'),
]

