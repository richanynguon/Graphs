from room import Room
from player import Player
from world import World
from stack import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "/home/creator/Desktop/CS/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
opposite_dir = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e',
}

visited = {player.current_room}
local_path = Stack()

while len(visited) < len(world.rooms):
    current_room = player.current_room
    last_room = player.current_room
    
    possible_rooms = player.current_room.get_exits()
    random.shuffle(possible_rooms)

    for direction in possible_rooms:
        possible_room = current_room.get_room_in_direction(direction)
        if possible_room == None:
            continue
        if possible_room not in visited:
            visited.add(possible_room)
            local_path.push(direction)
            traversal_path.append(direction)
            player.travel(direction)
            last_room = possible_room
            break                  
    if current_room == last_room:
        dir_to_last = opposite_dir[local_path.pop()]
        traversal_path.append(dir_to_last)
        player.travel(dir_to_last)


# visited= set()
# stack = Stack()
# stack.push([world.starting_room])
# while len(visited) < 500:
#     local_path = stack.pop()
#     current_node = local_path[-1]
#     try:
#         if current_node not in visited:
#             visited.add(current_node)
#             neighbor_nodes = set()
#             stored_direction = []

#             for direction in current_node.get_exits():
#                 room = current_node.get_room_in_direction(direction)
#                 stored_direction.append({"room": room, "dir": direction})
#                 neighbor_nodes.add(room)

#             unvisited_neighbors = neighbor_nodes - visited
#             if len(unvisited_neighbors) == 0:
#                 raise Exception
#             random_neighbor = random.sample(unvisited_neighbors, 1)[-1]
#             new_local = local_path.copy()
#             new_local.append(random_neighbor)

#             direction =  [stored for stored in stored_direction if stored["room"] == random_neighbor]

#             room_dir = direction[-1]["dir"]

#             traversal_path.append(room_dir)
#             stack.push(new_local)
#         else: raise Exception
#     except:
#         current_node = local_path[-1]
#         neighbor_nodes = set()
#         stored_direction = []

#         for direction in current_node.get_exits():
#             room = current_node.get_room_in_direction(direction)
#             stored_direction.append({"room": room, "dir": direction})
#             neighbor_nodes.add(room)

#         unvisited_neighbors = neighbor_nodes - visited
#         if len(unvisited_neighbors) == 0:
#             new_local = local_path[:-1]
#             last_node = new_local[-1]
#             stored_direction = []

#             for direction in last_node.get_exits():
#                 room = last_node.get_room_in_direction(direction)
#                 if room == current_node:
#                     stored_direction.append({"room": room, "dir": direction})

#             direction = stored_direction[-1]['dir']

#             back_dir =  opposite_dir[f"{direction}"]

#             traversal_path.append(back_dir)
#             stack.push(new_local)
#         else:
#             neighbor_nodes = set()
#             stored_direction = []

#             for direction in current_node.get_exits():
#                 room = current_node.get_room_in_direction(direction)
#                 stored_direction.append({"room": room, "dir": direction})
#                 neighbor_nodes.add(room)

#             unvisited_neighbors = neighbor_nodes - visited
#             random_neighbor = random.sample(unvisited_neighbors, 1)[-1]
#             new_local = local_path.copy()
#             new_local.append(random_neighbor)

#             direction =  [stored for stored in stored_direction if stored["room"] == random_neighbor]

#             room_dir = direction[-1]["dir"]

#             traversal_path.append(room_dir)
#             stack.push(new_local)



    '''

    im in a room
    i need to explore if there are rooms n, s, e, w
    then i will randomly pick one after surveying the rooms
    i'll go to the randomly picked one that i havent visited
    take a write down my path 
    i repeat until all my possible paths are already visited
    if this is true then backtrack to the room before until
    there are rooms i have not visited
    




    i start in room
    lay done some crumbs aka my current path in this room
    then i look for all exits
    if it leads to a room that I havent visited yet
    then i go there
    if i hit a room where there are only rooms that i've visted then i follow back my bread crumbs but i pick up my bread crumbs
    aka remove the last room on my current path
    then i check if i have rooms i can walk to if not then keep going back and removing my crumbs


    get all exits 
    i pick one that i havent visted
    keep track of the path i've taken
    enter room
    repeat until either there are no 

    '''


'''

room.get_exits return ["n", "w"]
room.get_room_in_direction returns room object

player.travel changes room
player.current_room will give room object

so maybe checking if this current room has neighbors they havent visited if so then go there
if not then keep backtracking


instantiate 
three trackers

local_path - this will go into the stack
traversal_path 
and visited

I am at current node
Store my current node in my 
lp, tp, and v
I want to get me neighbors
pick one that i havent visited before, add to local path and go there
repeat step 1 -4 
until there are no neighbors that you have not visited
then you keep popping off lp until v reaches to  500 rooms

    
old version



'''


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


######
# UNCOMMENT TO WALK AROUND
######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


#####
#                                                                                                                                                           #
#                                                        434       497--366--361  334--384--435  476                                                        #
#                                                         |                   |    |              |                                                         #
#                                                         |                   |    |              |                                                         #
#                                              477--443  425            386--354--321  338  313  380--445--446                                              #
#                                                    |    |              |         |    |    |    |    |                                                    #
#                                                    |    |              |         |    |    |    |    |                                                    #
#                                                   408  350  483  385  388  285  304  278  287--353  480                                                   #
#                                                    |    |    |    |    |    |    |    |    |                                                              #
#                                                    |    |    |    |    |    |    |    |    |                                                              #
#                                    442  461  426  392--281  223--169  257  253  240  196--224  255  373                                                   #
#                                     |    |    |         |         |    |    |    |    |         |    |                                                    #
#                                     |    |    |         |         |    |    |    |    |         |    |                                                    #
#                                    417  422--394--318--199--197--165--163--228  233--152  192--239--336--421                                              #
#                                     |              |                   |              |    |                                                              #
#                                     |              |                   |              |    |                                                              #
#                          491  453--351  444  374--340  328--200--204  148--178  143  147--154--184  282  363  389                                         #
#                           |         |    |                   |         |         |    |              |    |    |                                          #
#                           |         |    |                   |         |         |    |              |    |    |                                          #
#                          489  441  332  387  341--316  195  175--141  121--123--138--139--176  136--231--294--311--499                                    #
#                           |    |    |    |         |    |         |    |                        |                                                         #
#                           |    |    |    |         |    |         |    |                        |                                                         #
#                     396--391  319  295  331  307  292--185--155  107  111--114--120  172  146  109  186--262--390--398                                    #
#                           |    |    |    |    |              |    |    |              |    |    |    |              |                                     #
#                           |    |    |    |    |              |    |    |              |    |    |    |              |                                     #
#           452--428--411--324--289--250  277  208--166  140  082  102--064  101  093  132  086--095  098  245--343  487                                    #
#                 |                   |    |         |    |    |         |    |    |    |    |         |    |                                               #
#                 |                   |    |         |    |    |         |    |    |    |    |         |    |                                               #
#           451--429  397  357--342--221--174  210  161  063--061  033  060  091  051  073  084  078--090--142  381--431                                    #
#                      |                   |    |    |         |    |    |    |    |    |    |    |              |                                          #
#                      |                   |    |    |         |    |    |    |    |    |    |    |              |                                          #
#      492--400--399--358  352  297--207  124--112--106--079--046--017--028  037--042  056--067  075--088--125--238--293                                    #
#                      |    |         |                             |    |    |         |         |    |    |                                               #
#                      |    |         |                             |    |    |         |         |    |    |                                               #
#           414--365--333--303  171--168--137  085  074  032  047--014  030  031  027--055  048--053  103  198--270--300--320                               #
#                 |         |              |    |    |    |         |         |    |         |                             |                                #
#                 |         |              |    |    |    |         |         |    |         |                             |                                #
#                447  301--187--167--108--081--045--040--019--015--013--009  020--026  035--044--059--189--275--283--376  471                               #
#                                          |                             |    |         |                             |                                     #
#                                          |                             |    |         |                             |                                     #
#                436  470  227--194--128--092  069--041--036--021  004  007--012--018--034--039--071--150--251  325  468                                    #
#                 |    |              |    |    |    |         |    |    |         |         |    |              |                                          #
#                 |    |              |    |    |    |         |    |    |         |         |    |              |                                          #
#           465--368--284--254--205--162  100  072  076  011--003--000--001--022  024--025  052  115--160--214--246--412                                    #
#                      |                        |         |         |    |         |    |                                                                   #
#                      |                        |         |         |    |         |    |                                                                   #
#           479--418--349  274--222--190--129  089  083--080  016--008  002--010  029  043--049--119--131--329--407                                         #
#                 |                        |    |    |                   |    |    |    |         |                                                         #
#                 |                        |    |    |                   |    |    |    |         |                                                         #
#                463--458  379  226--225--105--104  099  058--023--006--005  038  054  077--130  219--305--330--454                                         #
#                      |    |    |              |    |         |    |    |                        |         |                                               #
#                      |    |    |              |    |         |    |    |                        |         |                                               #
#           486--462  359  266--260  235--158--126  122  068--057  062  050--070--087  182--211  242  326  348                                              #
#                 |    |                   |    |              |    |    |    |    |    |    |    |    |                                                    #
#                 |    |                   |    |              |    |    |    |    |    |    |    |    |                                                    #
#                367--344--230  243  180--164  135  145--113--094  065  066  116  117--170  248  286--288--498                                              #
#                           |    |              |    |         |    |    |    |    |         |    |                                                         #
#                           |    |              |    |         |    |    |    |    |         |    |                                                         #
#                339--314--220--215--177--156--149  183  153--097  134  096  159  127--173  272  309--377--456                                              #
#                 |                        |    |              |    |    |         |    |         |                                                         #
#                 |                        |    |              |    |    |         |    |         |                                                         #
#           482--404  258--236--216--213--209  191  188  157--110  144  179--201  212  202--249  371--430--440                                              #
#            |              |         |         |    |         |    |    |    |    |    |                                                                   #
#            |              |         |         |    |         |    |    |    |    |    |                                                                   #
#           484  433--372--263  271--217  241--193  151--133--118--218  181  206  229  267--302--402--403--439                                              #
#                           |    |         |    |         |         |         |    |                                                                        #
#                           |    |         |    |         |         |         |    |                                                                        #
#      494--457--355--312--299  310  327--256  203  247--234--259  252  244--232  237--370  364--401--427--474                                              #
#                      |    |         |    |    |    |    |    |    |    |    |              |    |    |                                                    #
#                      |    |         |    |    |    |    |    |    |    |    |              |    |    |                                                    #
#                437--347  356  469--362  279  269  369  280  291  261  264  265--273--298--360  420  438                                                   #
#                      |    |         |    |    |              |    |    |    |    |              |    |                                                    #
#                      |    |         |    |    |              |    |    |    |    |              |    |                                                    #
#                393--375  405  423--395  323  315--335--378  306  345  290  268  296--308--337  464  448--490                                              #
#                      |    |                   |    |    |    |    |         |    |    |    |         |                                                    #
#                      |    |                   |    |    |    |    |         |    |    |    |         |                                                    #
#           493--478--413  432--473       410--406  346  466  415  409  322--276  382  317  383       475                                                   #
#                      |    |                             |         |    |    |    |    |    |         |                                                    #
#                      |    |                             |         |    |    |    |    |    |         |                                                    #
#                     419  449--450                      472--495  488  424  459  455  416  460       496                                                   #
#                                                         |                   |                                                                             #
#                                                         |                   |                                                                             #
#                                                   485--481                 467                                                                            #
#                                                                                                                                                           #
#####
