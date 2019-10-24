from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('call_map', api.call_map),
    url('call_items', api.call_items),
    url('check_items', api.check_room_for_item),
    url('check_inventory', api.check_inventory),
    url('get_item', api.get_item_from_room),
    url('drop_item', api.drop_item)
]