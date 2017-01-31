class weapon(object):
	"""Quest weapon creator"""
	def __init__(self, name, damage, protection, healing, dousing, sacrificial_lamb):
		self.name = name
		self.damage = damage
		self.protection = protection
		self.healing = healing
		self.dousing = dousing
		self.sacrificial_lamb = sacrificial_lamb
		
Battleaxe = weapon("Battleaxe", 35, 5, 0, 0, 0)
Shield = weapon("Shield", 7, 25, 0, 5, 0)
Armour = weapon("Armour", 0, 30, 0, 10, 0)
Healingpotion = weapon("Healing Potion", 0, 0, 50, 0, 0)
Fire = weapon("Fire", 25, 5, 0, 0, 0)
Water = weapon("Water", 0, 0, 0, 25, 0)
DonaldTrump = weapon("Donald Trump", 0, 0, 0, 0, 100)

def arena():
	



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

		
	print "you have chosen: " + item_1.name
	print
	inventory.append(item_1)
	print
	print item_1.name + " has been added to your inventory"
	print
		
	item_2 = raw_input("What is your first choice? 1-10:-   ")
	if item_2 == "1":
		item_2 = Battleaxe
	elif item_2 == "2":
		item_2 = Shield
	elif item_2 == "3":
		item_2 = Armour	
	elif item_2 == "4":		
		item_2 = Healingpotion	
	elif item_2 == "5":		
		item_2 = Fire
	elif item_2 == "6":
		item_2 = Water
	elif item_2 == "7":
		item_2 = DonaldTrump
	print
	while len(inventory) < 2:
		if item_2 == item_1:
			print "You fool, you have already chosen this item! You need to pick again"
			item_2 = raw_input("I ask you again, What is your second choice? 1-10:-   ")
			if item_2 == "1":
				item_2 = Battleaxe
			elif item_2 == "2":
				item_2 = Shield
			elif item_2 == "3":
				item_2 = Armour	
			elif item_2 == "4":		
				item_2 = Healingpotion	
			elif item_2 == "5":		
				item_2 = Fire
			elif item_2 == "6":
				item_2 = Water
			elif item_2 == "7":
				item_2 = DonaldTrump
		else:
			print "you have chosen: "+ item_2.name
			inventory.append(item_2)
		print
		print item_2.name + " has been added to your inventory"
		print
	item_3 = raw_input("What is your third choice? 1-10:-    ")
	if item_3 == "1":
		item_3 = Battleaxe
	elif item_3 == "2":
		item_3 = Shield
	elif item_3 == "3":
		item_3 = Armour	
	elif item_3 == "4":		
		item_3 = Healingpotion	
	elif item_3 == "5":		
		item_3 = Fire
	elif item_3 == "6":
		item_3 = Water
	elif item_3 == "7":
		item_3 = DonaldTrump
	
	while len(inventory) < 3:
		print
		if item_3 == item_1:
			print "You fool, you have already chosen this item! You need to pick again"
			item_3 = raw_input("I ask you again, What is your third choice? 1-10:-   ")
			if item_3 == "1":
				item_3 = Battleaxe
			elif item_3 == "2":
				item_3 = Shield
			elif item_3 == "3":
				item_3 = Armour	
			elif item_3 == "4":		
				item_3 = Healingpotion	
			elif item_3 == "5":		
				item_3 = Fire
			elif item_3 == "6":
				item_3 = Water
			elif item_3 == "7":
				item_3 = DonaldTrump
		elif item_3 == item_2:
			print "You fool, you have already chosen this item! You need to pick again"
			item_3 = raw_input("I ask you again, What is your third choice? 1-10:-   ")
			if item_3 == "1":
				item_3 = Battleaxe
			elif item_3 == "2":
				item_3 = Shield
			elif item_3 == "3":
				item_3 = Armour	
			elif item_3 == "4":		
				item_3 = Healingpotion	
			elif item_3 == "5":		
				item_3 = Fire
			elif item_3 == "6":
				item_3 = Water
			elif item_3 == "7":
				item_3 = DonaldTrump
		else:
			print "you have chosen: "+ item_3.name
			inventory.append(item_3)
			print
			print item_3.name + " has been added to your inventory"
			print
	print "Your inventory contains"
	for item in inventory:
		print item.name
			
		
	print """ It is time to proceed.
		
		Good Luck
		
		(You'll need it!)"""
		
	print """ You are in the Death Match Arena!
	
	You are in the mddle of a small, empty room, the room has 2 doors....
	
	Door 1 is a huge, red, wooden door with an engraving of a Panda on it
	
	Door 2 is small and metalic and has a picture of a horse
	
	Which door do you choose?
	
	1 or 2 """
	
	firstdoor = raw_input()
	if firstdoor =="1":
		print "The door opens with an onimous creek"	
		Panda()
	elif firstdoor == "2":
		print "The door flies open with a BANG!"
		print """in front of you stands a huge warrior holding a sword
		he also appears to be made out of paper
		
		It's time to decide what to do
		
		1 - run back the way you came
		
		2 - fight him!"""
		horse_answer = raw_input()
		if horse_answer == "1":
			print "you chose to run"
			print "you turn and flee"
			print			
			arena()
		elif horse_answer == "2":
			print "you have chosen to fight"
			print "and fight you shall"
			print "make you move"
			print "Your inventory contains"
			for item in inventory:
			print item.name
			print "What item do you choose?"
			horsechoice1 = raw_input()
			if horsechoice1 == Fire:
				print "You have burned the warrior down and may procede"
				horse(2)
			elif horsechoice1 == DonaldTrump:
				print """Don't you know that Donanld Trump is useless in all but the most desperate situations?!
				The warrior dispatches you in one swipe of his sword!
				YOU ARE DEAD - YOU DID NOT SURVIVE THE DEATH MATCH
				GAME OVER!!!!!!!!"""
		
	#print "your first item is " + item_1.name
	#print "it's values are as follows:"
	#print "Name " + item_1.name
	#print "Damage:  " +str(item_1.damage)
	#print "protection: " +str(item_1.protection)
	#print "healing: " +str(item_1.healing)
	#print "dousing: " +str(item_1.dousing)
	#print "sacrificial_lamb: " +str(item_1.sacrificial_lamb)

	
	
	

	
		
game_3()