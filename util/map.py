from django.contrib.auth.models import User
from adventure.models import Player, Room, Item

Item.objects.all().delete()

item_dict = {
    "Sword": Item(item_name="Big Sword", item_description="This is heavy", is_key=False),
    "Chest Key": Item(item_name="Chest Key", item_description="It opens chests", is_key=True)
}

for item in item_dict.values():
    item.save()

Room.objects.all().delete()

room_dict = {
"r0_0" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=0, items={item_dict['Sword'].item_name:item_dict["Sword"].item_description}),
"r0_1" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=0),
"r0_2" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=0),
"r0_3" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=0),
"r0_4" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=0),
"r0_5" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=0),
"r0_6" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=0),
"r0_7" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=0),
"r0_8" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=0),
"r0_9" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=0),
"r0_10" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=0),
"r0_11" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=0),
"r0_12" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=0),
"r0_13" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=0),
"r0_14" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=0),

"r1_0" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=1),
"r1_1" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=1),
"r1_2" : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=1),
'r1_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=1),
'r1_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=1),
'r1_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=1),
'r1_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=1),
'r1_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=1),
'r1_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=1),
'r1_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=1),
'r1_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=1),
'r1_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=1),
'r1_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=1),
'r1_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=1),
'r1_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=1),

'r2_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=2),
'r2_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=2),
'r2_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=2),
'r2_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=2),
'r2_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=2),
'r2_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=2),
'r2_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=2),
'r2_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=2),
'r2_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=2),
'r2_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=2),
'r2_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=2),
'r2_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=2),
'r2_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=2),
'r2_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=2),
'r2_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=2),

'r3_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=3),
'r3_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=3),
'r3_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=3),
'r3_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=3),
'r3_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=3),
'r3_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=3),
'r3_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=3),
'r3_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=3),
'r3_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=3),
'r3_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=3),
'r3_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=3),
'r3_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=3),
'r3_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=3),
'r3_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=3),
'r3_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=3),

'r4_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=4),
'r4_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=4),
'r4_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=4),
'r4_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=4),
'r4_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=4),
'r4_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=4),
'r4_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=4),
'r4_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=4),
'r4_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=4),
'r4_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=4),
'r4_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=4),
'r4_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=4),
'r4_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=4),
'r4_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=4),
'r4_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=4),

'r5_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=5),
'r5_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=5),
'r5_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=5),
'r5_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=5),
'r5_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=5),
'r5_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=5),
'r5_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=5),
'r5_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=5),
'r5_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=5),
'r5_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=5),
'r5_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=5),
'r5_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=5),
'r5_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=5),
'r5_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=5),
'r5_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=5),

'r6_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=6),
'r6_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=6),
'r6_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=6),
'r6_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=6),
'r6_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=6),
'r6_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=6),
'r6_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=6),
'r6_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=6),
'r6_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=6),
'r6_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=6),
'r6_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=6),
'r6_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=6),
'r6_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=6),
'r6_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=6),
'r6_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=6),

'r7_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=7),
'r7_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=7),
'r7_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=7),
'r7_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=7),
'r7_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=7),
'r7_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=7),
'r7_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=7),
'r7_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=7),
'r7_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=7),
'r7_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=7),
'r7_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=7),
'r7_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=7),
'r7_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=7),
'r7_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=7),
'r7_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=7),

'r8_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=8),
'r8_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=8),
'r8_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=8),
'r8_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=8),
'r8_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=8),
'r8_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=8),
'r8_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=8),
'r8_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=8),
'r8_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=8),
'r8_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=8),
'r8_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=8),
'r8_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=8),
'r8_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=8),
'r8_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=8),
'r8_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=8),

'r9_0' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=0, y_coord=9),
'r9_1' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=1, y_coord=9),
'r9_2' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=2, y_coord=9),
'r9_3' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=3, y_coord=9),
'r9_4' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=4, y_coord=9),
'r9_5' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=5, y_coord=9),
'r9_6' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=6, y_coord=9),
'r9_7' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=7, y_coord=9),
'r9_8' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=8, y_coord=9),
'r9_9' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=9, y_coord=9),
'r9_10' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=10, y_coord=9),
'r9_11' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=11, y_coord=9),
'r9_12' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=12, y_coord=9),
'r9_13' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=13, y_coord=9),
'r9_14' : Room(title='grass_tile', description='grass_tile', tile='grass1', x_coord=14, y_coord=9)
}

for room in room_dict.values():
    room.save()


def room_linker(room_dict, x_max, y_max):
    for room in room_dict.values():

        if room.x_coord > 0 and room.x_coord < x_max and room.y_coord > 0 and room.y_coord < y_max:

            north = 'r'+str(room.y_coord+1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[north], "n")

            south = 'r'+str(room.y_coord-1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[south], "s")

            east = 'r'+str(room.y_coord)+'_'+str(room.x_coord+1)
            room.connectRooms(room_dict[east], "e")

            west = 'r'+str(room.y_coord)+'_'+str(room.x_coord-1)
            room.connectRooms(room_dict[west], "w")

        elif room.x_coord == 0 and room.y_coord > 0 and room.y_coord < y_max:

            north = 'r'+str(room.y_coord+1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[north], "n")

            south = 'r'+str(room.y_coord-1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[south], "s")

            east = 'r'+str(room.y_coord)+'_'+str(room.x_coord+1)
            room.connectRooms(room_dict[east], "e")

        elif room.x_coord == x_max and room.y_coord > 0 and room.y_coord < y_max:

            north = 'r'+str(room.y_coord+1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[north], "n")

            south = 'r'+str(room.y_coord-1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[south], "s")

            west = 'r'+str(room.y_coord)+'_'+str(room.x_coord-1)
            room.connectRooms(room_dict[west], "w")

        elif room.y_coord == 0 and room.x_coord > 0 and room.x_coord < x_max:

            north = 'r'+str(room.y_coord+1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[north], "n")

            east = 'r'+str(room.y_coord)+'_'+str(room.x_coord+1)
            room.connectRooms(room_dict[east], "e")

            west = 'r'+str(room.y_coord)+'_'+str(room.x_coord-1)
            room.connectRooms(room_dict[west], "w")    

        elif room.y_coord == y_max and room.x_coord > 0 and room.x_coord < x_max:

            south = 'r'+str(room.y_coord-1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[south], "s")

            east = 'r'+str(room.y_coord)+'_'+str(room.x_coord+1)
            room.connectRooms(room_dict[east], "e")

            west = 'r'+str(room.y_coord)+'_'+str(room.x_coord-1)
            room.connectRooms(room_dict[west], "w") 

        elif room.x_coord == 0 and room.y_coord == 0:
            north = 'r'+str(room.y_coord+1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[north], "n")

            east = 'r'+str(room.y_coord)+'_'+str(room.x_coord+1)
            room.connectRooms(room_dict[east], "e")

        elif room.x_coord == 0 and room.y_coord == y_max:

            south = 'r'+str(room.y_coord-1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[south], "s")

            east = 'r'+str(room.y_coord)+'_'+str(room.x_coord+1)
            room.connectRooms(room_dict[east], "e") 

        elif room.x_coord == x_max and room.y_coord == 0:
            north = 'r'+str(room.y_coord+1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[north], "n")

            west = 'r'+str(room.y_coord)+'_'+str(room.x_coord-1)
            room.connectRooms(room_dict[west], "w")   

        elif room.x_coord == x_max and room.y_coord == y_max:

            south = 'r'+str(room.y_coord-1)+'_'+str(room.x_coord)
            room.connectRooms(room_dict[south], "s")

            west = 'r'+str(room.y_coord)+'_'+str(room.x_coord-1)
            room.connectRooms(room_dict[west], "w") 

room_linker(room_dict, 14, 9)

players=Player.objects.all()
for p in players:
  p.currentRoom=room_dict['r0_0'].id
  p.save()