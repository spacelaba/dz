# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:47:26 2023

@author: Ilya
"""

a = input("How many games did you won per day? ")
b = input("How many games did you lose per day? ")
print("Your winrate: " + str(int(a)/(int(a)+int(b))*100) + "%");