def game_3():
	print """ 
	
Welcome to the final round of your Epic quest......

A FIGHT TO THE DEATH!!!!!!!

"""

	ready = raw_input("Are you ready to play? yes - I'm ready let's go / no - I'm scared!").lower()
	if ready == "yes":
		print """
		
		
		THEN PREPARE TO DIE!!!!
		
		
		"""
	elif ready == "no":
		print """
		
		There is no turning back now, PREPARE TO DIE!!!!
		
		
		"""
	else:
		print """
		
		
		I see the fear has taken away your ability to answer my question, it matters not, PREPARE TO DIE!!!!!!
		
		
		"""
	death_match()

def death_match():
	inventory = []
	Battleaxe = {'damage':35, 'protection':5,'healing':0, 'cooling':0, 'sacrificial_lamb':0,}
	Shield = {'damage':7, 'protection':25,'healing':0, 'cooling':5, 'sacrificial_lamb':0,}
	Armour = {'damage':0, 'protection':30,'healing':0, 'cooling':10, 'sacrificial_lamb':0,}
	Healingpotion = {'damage':0, 'protection':0,'healing':50, 'cooling':0, 'burning':0, 'sacrificial_lamb':0,}
	Fire = {'damage':25, 'protection':0,'healing':0, 'cooling':0, 'sacrificial_lamb':0,}
	Water = {'damage':0, 'protection':0,'healing':0, 'cooling':25, 'sacrificial_lamb':0,}
	DonaldTrump = {'damage':0, 'protection':0,'healing':0, 'cooling':0, 'sacrificial_lamb':100,}
	options = Battleaxe


	
	print """You may choose 3 items from the following list to help you in battle, choose wisely!:
		
	1 - Battleaxe
	2 - Shield
	3 - Armour
	4 - Healing potion
	5 - fire
	6 - water
	7 - Donald Trump
	
	"""
	
	
	
	item_1 = raw_input("What is your first choice? 1-10:-   ")
	
	if item_1 == "1":
		item_1 = Battleaxe
	elif item_1 == "2":
		item_1 = Shield
	elif item_1 == "3":
		item_1 = Armour
	elif item_1 == "4":
		item_1 = Healingpotion
	elif item_1 == "5":
		item_1 = Fire
	elif item_1 == "6":
		item_1 = Water
	elif item_1 == "7":
		item_1 = DonaldTrump
	
	print dict(item_1)
	print
	inventory.append [item_1]
	print
	print item_1 + " has been added to your inventory"
	print
	
	item_2 = raw_input("What is your first choice? 1-10:-   ")
	print
	while len(inventory) < 2:
		if item_2 == item_1:
			print "You fool, you have already chosen this item! You need to pick again"
			item_2 = raw_input("I ask you again, What is your second choice? 1-10:-   ")
		else:
			print "you have chosen: "+ options[item_2]
			inventory.append(options[item_2])
		print
		print options[item_2] + " has been added to your inventory"
		print
	item_3 = raw_input("What is your third choice? 1-10:-    ")
	while len(inventory) < 3:
		print
		if item_3 == item_1:
			print "You fool, you have already chosen this item! You need to pick again"
			item_3 = raw_input("I ask you again, What is your third choice? 1-10:-   ")
		elif item_3 == item_2:
			print "You fool, you have already chosen this item! You need to pick again"
			item_3 = raw_input("I ask you again, What is your third choice? 1-10:-   ")
		else:
			print "you have chosen: "+ options[item_3]
			inventory.append(options[item_3])
			print
			print options[item_3] + " has been added to your inventory"
			print
	print "Your inventory contains"
	for item in inventory:
		print item
		
	print
	print """ It is time to proceed.
	
	Good Luck
	
	(You'll need it!)"""
		   
game_3()	