#!/usr/bin/python3.8

#    babe_vs_maris.py: simulate the chances of Maris beating Babe Ruth record according to 
#                      Leonard Mlodinow's Dunkard's Walk book (Chapter 1).

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
from collections import Counter
import matplotlib.pyplot as plt

mat = [0 for x in range(147)]

total_seasons_c = 100000

list_filled = [] 
random_position = 0
for i in range(10): #just fill the homerun hit position also random 
    random_position = random.randint(0,146)
    while(random_position in list_filled): #check if the position wasn't chosen already. See [1].
        random_position = random.randint(0,146)
    
    list_filled.append(random_position)     
    mat[random_position] = 1

record_seasons=0

hr_per_season = []

for j in range(total_seasons_c): 
    home_runs = 0  
    for i in range(int(698)): #see [1]
        home_runs += mat[random.randint(0,146)] #if HR, sum 1, if not 0. 
    if(home_runs >= 61):
      record_seasons += 1
    hr_per_season.append(home_runs)
    
    if (j % 1000==0):
      print("Total seasons=",j," - More than 60 HRs so far=",record_seasons)

print("Total seasons with Maris broking Babe Ruth record", record_seasons, "in",total_seasons_c, "seasons (simulations). It means "+str(round((record_seasons/total_seasons_c*100),2))+"% chance")

print("In this universe of", total_seasons_c,"seasons, Maris would have broken Babe Ruth record once every", round(1/(record_seasons/total_seasons_c),2))    

occurrences = Counter(hr_per_season)  

plt.bar(*zip(*occurrences.items()))
plt.show()

# [1] According to Leonard Mlodinow's Drunkard's Walk book (Chapter 1), Maris had a stat in 1960 season of 1 HR in 14.7 (or 10 in 147). Using this value here to
#     check how hard is for him to beat Babe Ruth record.  
# [2] The number 698 represent the number o chances to hit a HR that Maris had in 1961 season and it was taken from https://sigmazone.com/quantum_xl_multiple_inputs/
#     because I don't know enough of baseball to do it myself. 

# Final Comment: While both Mlodinow and Philip Mayfield from Sigmazone reached similar results of Maris broking Babe Ruth record once every ~32 seasons, my code reached
#                once every ~35 seasons (due randomness and method, probably), which I believe it's good enough for sharing it in my github. :) 
#                On purpose, I let the round(...,2) in the last printed line instead of rounding it down when it's like 35.2 or up when it's 35.6, everybody that reach 
#                here will be able to correct interpreted that. 

