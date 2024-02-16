# Colin Beary CSC119 Spring 2021

import time		# used to add wait time during printing
from termcolor import cprint 	# print in different colors
import random

goblin = 1
imp = 2
mage = 3

user_hp = 20

def hp():
	global user_hp
	
	if user_hp < 5:
		cprint("HP: " + user_hp, "red")
	elif user_hp < 10:
		cprint("HP: " + user_hp, "yellow")
	elif user_hp < 15:
		cprint("HP: " + user_hp, "green")
	else:
		cprint("HP: " + user_hp, "blue")

#gives odds for encountering an enemy, if a room has the ability to encounter an enemy
def encounter(enemy):
	if enemy == "goblin":
		enemychance = 80
	elif enemy == "imp":
		enemychance = 50
	elif enemy == "mage":
		enemychance = 30
	
	encounter_check = random.randint(1,101)
	
	if encounter_check <= enemychance:
		print()
		cprint("A " + enemy + " appears!", "yellow")
		time.sleep(.5)
		combat(enemy)
	


#defines combat statistics for the enemies, and ensures the function will end once the enemies hp reaches 0
def combat(enemy):
	global user_hp
	if enemy == "goblin":
		global goblin
		enemy_hp = goblin
	elif enemy == "imp":
		global imp
		enemy_hp = imp
	elif enemy == "mage":
		global mage
		enemy_hp = mage

	while enemy_hp > 0 and user_hp > 0:
		print()
		userattack(enemy_hp)
		enemy_hp -= (user_dmg)
		if enemy_hp <=0:
			cprint("You defeated the " + enemy + "!", "green")
			break
		time.sleep(.5)
		print()
		
		enemyattack(enemy)
		user_hp -= (dmg)
		if user_hp <=0:
			cprint("The " + enemy + " has beaten you. Game over!")
			break
		time.sleep(.5)
		print()
	
		
d20 = 20
	

def roll():
	global d20
	d20 = random.randint(1,21)


def userattack(enemy_hp):

	print("You attack!")
	roll()
	global d20
	user_swing = d20
	global user_dmg
	if user_swing == 20:
		print("You land a nasty blow. You deal 2 points of damage!")
		user_dmg = 2
	elif user_swing >= 10:
		print("You catch the enemy with your weapon. You deal 1 point of damage")
		user_dmg = 1
	else:
		print("Your swing goes wide. Miss!")
		user_dmg = 0

def enemyattack(enemy):
	global user_hp

	if enemy == "goblin":
		global goblin
		enemy_dmg = goblin
	elif enemy == "imp":
		global imp
		enemy_dmg = imp
	elif enemy == "mage":
		global mage
		enemy_dmg = mage
	global dmg
	print("The " + enemy + " attacks!")
	
	roll()
	global d20
	enemy_swing = d20
	if enemy_swing == 20:
		cprint("The " + enemy + " deals a nasty blow! ouch!", "red")
		dmg = (enemy_dmg*2)
	elif (enemy_swing + enemy_dmg) >= 16:
		print("The " + enemy + " lands a hit. Darn!")
		dmg = enemy_dmg
	else:
		print("The " + enemy + " misses!")
		dmg = 0
