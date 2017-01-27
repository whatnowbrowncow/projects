
def play():
	print "Hello", name
	print "Would you like to play a game? Yes or No?"
	answer = raw_input().lower()
	if answer == "yes":
		print "ok then, let's get started"
		game_1()
	elif answer == "no":
		are_you_sure()
	else:
		print "You didn't type yes or no!"
		play()
		
def are_you_sure():
	print "Are you shure you don't wan't to play?"
	print "Type Y to be sure and quit or type N to hear the first question again"
	final_answer = raw_input().lower()
	if final_answer == "y":
		print "Goodbye then spoil sport!"
	elif final_answer == "n":
		play()

def game_1():
	correct = False
	print "WELCOME %s TO THE WORLDS GREATEST GAME!!!!" % (name)
	print "First a riddle to see if you are worthy!"
	print "you have 3 tries"
	print "I can go up a chimney down but not down a chimney up..........What am I?"
	worthy = raw_input().lower()
	for tries in range(2):
		if worthy == "umbrella":
			print "congratulations %s you are indeed worthy" % (name)
			correct = True
			game_2()
		else:
			print worthy, "is wrong, try again"
			worthy = raw_input().lower()

	print "Last chance!"
	worthy = raw_input().lower()
	print worthy
	if worthy == "umbrella":
		print "congratulations %s you are indeed worthy" % (name)
		game_2() 
	else:
		print "Sorry %s, you are not worthy, GAME OVER!" % (name)
		
def game_2():
	print "check back later for the next round"

name = raw_input("what is your name?")
play()