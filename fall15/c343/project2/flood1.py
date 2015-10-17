from utilities import *

def check(color_of_tile,flooded_list,tile,screen_size):
	targets = list()
	if in_bounds(up(tile),screen_size):
		if not (up(tile) in flooded_list) and (color_of_tile[tile] == color_of_tile[up(tile)]):
			targets.append(up(tile))
	if in_bounds(left(tile),screen_size):
		if not (left(tile) in flooded_list) and (color_of_tile[tile] == color_of_tile[left(tile)]):
			targets.append(left(tile))
	if in_bounds(down(tile),screen_size):
		if not (down(tile) in flooded_list) and (color_of_tile[tile] == color_of_tile[down(tile)]):
			targets.append(down(tile))
	if in_bounds(right(tile),screen_size):
		if not (right(tile) in flooded_list) and (color_of_tile[tile] == color_of_tile[right(tile)]):
			targets.append(right(tile))
	return targets

def flood(color_of_tile,flooded_list,screen_size):
	to_fill = list()
	for t in flooded_list:
		to_fill = check(color_of_tile,flooded_list ,t,screen_size)
	flooded_list += to_fill
	if len(to_fill) != 0:
		flood(color_of_tile,flooded_list,screen_size)
