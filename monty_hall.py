#!/usr/bin/python3.8

#    monty_hall.py: simulate the Monty Hall problem mentioned in 
#                   Leonard Mlodinow's Dunkard's Walk book (Chapter 3). 
#                   If you want a different version with more doors you can find one at
#                   https://scipython.com/book/chapter-4-the-core-python-language-ii/examples/the-monty-hall-problem/

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = "Josué P. J. de Freitas"
__license__ = "GPL"
__email__ = "josue.freitas@gmail.com"

#Original avaiable at https://github.com/josuepjfreitas/drunkards_walk

import random

total_doors_c = 3

doors = [0, 0, 0] #0 means goat, 1 means car/prize

total_runs_c = 1000 


def place_car_in_one_door(): 
    global doors
    doors = [0, 0, 0]
    
    doors[random.randint(0,2)] = 1


def contestant_choose_door():
    return random.randint(0,2)


def show_host_choose_door(): 
    global contestant_door
    for door_number in range(total_doors_c):
        if door_number != contestant_door and doors[door_number]==0: # if it's not the door the contestant chose and the car is not behind it, choose it
            return door_number
    


def contestant_change_door(): 
    global contestant_door
    global show_host_door
    for door_number in range(total_doors_c):
        if door_number != contestant_door and door_number != show_host_door: #pick a door that's not the door initial selected and not the show host door that does not contain the prize
            return door_number            



total_prizes = 0

for i in range(total_runs_c):
    place_car_in_one_door()

    contestant_door = contestant_choose_door()

    show_host_door = show_host_choose_door()

    contestant_door = contestant_change_door()

    if doors[contestant_door]==1:
        total_prizes += 1

print("Win rate changing the door:", total_prizes/total_runs_c)

total_prizes = 0 

for i in range(total_runs_c):
    place_car_in_one_door()

    contestant_door = contestant_choose_door()

    show_host_door = show_host_choose_door()

    if doors[contestant_door]==1:
        total_prizes += 1

print("Win rate NOT changing the door:", total_prizes/total_runs_c)
