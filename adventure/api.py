from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from django.http import JsonResponse
from django.http import HttpResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json


from django.core import serializers

#instantiate pusher
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


@api_view(["GET"])
def call_map(request):
    data = Room.objects.all().values()
    return JsonResponse({"call_map":list(data)})

@api_view(["GET"])
def call_items(request):
    data = Item.objects.all().values()
    return JsonResponse({"call_items":list(data)})

@api_view(["GET"])
def check_room_for_item(request):
    player = request.user.player
    cur_room = Room.objects.get(id=player.currentRoom)
    item_id = dict(cur_room.items)
    empt_lst = []
    for i in item_id.keys():
        items = Item.objects.get(id=i)
        empt_lst.append([items.item_name, items.item_description, items.is_key])
    return JsonResponse({"items_in_room": empt_lst})

@api_view(["GET"])
def check_inventory(request):
    player = request.user.player
    item_id = dict(player.items)
    empt_lst = []
    for i in item_id.keys():
        items = Item.objects.get(id=i)
        empt_lst.append([items.item_name, items.item_description, items.is_key])
    return JsonResponse({"items_in_inventory": empt_lst})

@api_view(["POST"])
def get_item_from_room(request):
    player = request.user.player
    room = Room.objects.get(id=player.currentRoom)

    data = json.loads(request.body)
    item_picked = data['item']

    player_item_dict = dict(player.items)
    room_item_dict = dict(room.items)

    for id_, item_name in room_item_dict.items():
        if item_picked == item_name:
            player.items[id_] = item_name
            player.save()
            room.items.pop(id_)
            room.save()
            return JsonResponse({'item_swapped':"success"})
        else:
            return JsonResponse({'item_swapped':"not success"})

@api_view(["POST"])
def drop_item(request):
    player = request.user.player
    room = Room.objects.get(id=player.currentRoom)

    data = json.loads(request.body)
    item_picked = data['item']

    player_item_dict = dict(player.items)
    room_item_dict = dict(room.items)

    for id_, item_name in player_item_dict.items():
        if item_picked == item_name:
            room.items[id_] = item_name
            room.save()
            player.items.pop(id_)
            player.save()
            return JsonResponse({'item_dropped':"success"})
        else:
            return JsonResponse({'item_dropped':"not success"})




@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        for p_uuid in currentPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        for p_uuid in nextPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)
