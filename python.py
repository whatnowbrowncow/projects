
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
	for tries in range(2):
		worthy = raw_input().lower()
		if worthy == "umbrella":
			print "congratulations %s you are indeed worthy" % (name)
			correct = True
			game_2()
			break
		else:
			print worthy, "is wrong, try again"
	if correct == False:
		print "Last chance!"
		worthy = raw_input().lower()
		if worthy == "umbrella":
			print "congratulations %s you are indeed worthy" % (name)
			game_2() 
		else:
			print "Sorry %s, you are not worthy, GAME OVER!" % (name)
		
def game_2():
	print
	print
	print
	print
	print "Hello %s. Welcome to round two!" %(name)
	print
	print
	print "This round is a best of 3 game of rock paper scissors!"
	print "The rules are simple:"
	print "- You choose Rock, Paper or Scissors"
	print "- I will do the same"
	print
	print "- Rock beats Scissors"
	print "- Scissors beats Paper"
	print "- Paper beats Rock"
	print
	print "best of 3 wins"
	print
	print
	print "Are you ready to play? (y/n)"
	game_2_answer = raw_input().lower()
	if game_2_answer == "y":
		print "Ok lets Go!"
		rps()
	else:
		print "what is it? do you need a minute to compose yourself or something?"
		print "Ok fine"
		print "."
		print ".."
		print "..."
		print "...."
		print "....."
		print "......"
		print "......."
		print "........"
		print "........."
		print ".........."
		print " Right let's get on with it!"
		rps()

def rps():
	from random import randint
	print "ROCK - PAPER - Scissors"
	game = 1
	compscore = 0
	playerscore = 0
	result = 0
	for games in range(3):
		print "This is game number", game, "The current score is", "me", compscore, "you", playerscore
		print "what do you choose? (1/2/3)"
		print " 1 = Rock"
		print " 2 = Paper"
		print " 3 = Scissors"
		playernum = int(raw_input())
		if playernum == 1:
			playerchoice = "Rock"
		elif playernum == 2:
			playerchoice = "Paper"
		elif playernum == 3:
			playerchoice = "Scissors"
		else:
			print "selection not recognised"
		comprandom = randint(1, 4)
		if comprandom == 1:
			compchoice = "Rock"
		elif comprandom == 2:
			compchoice = "Paper"
		elif comprandom == 3:
			compchoice = "Scissors"
		print "3, 2, 1 GO!"
		print "You have chosen", playerchoice, "I have chosen", compchoice
		if compchoice == "Rock" and playerchoice == "Paper":
			print "Paper beats Rock, You Win!"
			playerscore = playerscore + 1
		elif compchoice == "Rock" and playerchoice == "Scissors":
			print "Rock beats Scissors, I Win!"
			compscore = compscore + 1
		elif compchoice == "Paper" and playerchoice == "Scissors":
			print "Scissors beats Paper, You Win!"
			playerscore = playerscore + 1
		elif compchoice == "Paper" and playerchoice == "Rock":
			print "Paper beats Rock, I Win!"
			compscore = compscore + 1
		elif compchoice == "Scissors" and playerchoice == "Rock":
			print "Scissors beats Rock, You Win!"
			playerscore = playerscore + 1
		elif compchoice == "Scissors" and playerchoice == "Paper":
			print "Scissors beats Paper, I Win!"
			compscore = compscore + 1
		else:
			print "we Both picked the same, it's a draw, we need to pick again!"
			def retry():
				rcompscore = 0
				rplayerscore = 0
				from random import randint
				playernum = int(raw_input())
				if playernum == 1:
					playerchoice = "Rock"
				elif playernum == 2:
					playerchoice = "Paper"
				elif playernum == 3:
					playerchoice = "Scissors"
				else:
					print "selection not recognised"
				comprandom = randint(1, 4)
				if comprandom == 1:
					compchoice = "Rock"
				elif comprandom == 2:
					compchoice = "Paper"
				elif comprandom == 3:
					compchoice = "Scissors"
				print "3, 2, 1 GO!"
				print "You have chosen", playerchoice, "I have chosen", compchoice
				if compchoice == "Rock" and playerchoice == "Paper":
					result = 1
					print "Paper beats Rock, You Win!"
					rplayerscore = rplayerscore + 1
					return result
				elif compchoice == "Rock" and playerchoice == "Scissors":
					result = 2
					print "Rock beats Scissors, I Win!"
					rcompscore = rcompscore + 1
					return result
				elif compchoice == "Paper" and playerchoice == "Scissors":
					result = 1
					print "Scissors beats Paper, You Win!"
					rplayerscore = rplayerscore + 1
					return result
				elif compchoice == "Paper" and playerchoice == "Rock":
					result = 2
					print "Paper beats Rock, I Win!"
					rcompscore = rcompscore + 1
					return result
				elif compchoice == "Scissors" and playerchoice == "Rock":
					result = 1
					print "Scissors beats Rock, You Win!"
					rplayerscore = rplayerscore + 1
					return result
				elif compchoice == "Scissors" and playerchoice == "Paper":
					result = 2
					print "Scissors beats Paper, I Win!"
					rcompscore = rcompscore + 1
					return result
				else:
					print "we Both picked the same, it's a draw!"
					retry()
			result = retry()
			print result
		if result == 1:
			playerscore = playerscore + 1
		elif result == 2:
			compscore = compscore + 1
		result = 0
		game = game + 1
	print "The final score is", "me", compscore, "you", playerscore
	if compscore > playerscore:
		print "I have emerged victorious from this round and you %s, are out of the game"%(name)
		print "!!!!!!!!!!!!!!!GAME OVER!!!!!!!!!!!!!!!!!"
	else:
		print "CONGRATULATIONS %s, You have won this round and get to progress to the final round......"%(name)
		print "!!!!!!!!!!!!!!!!!THE DEATH MATCH!!!!!!!!!!!!!!"
		print """
         _,.-------.,_
     ,;~'             '~;, 
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; | 
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   | 
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~. 
 |     ---;' / | \ `;---     |  
  \__.       \/^\/       .__/  
   V| \                 / |V  
    | |T~\___!___!___/~T| |  
    | |`IIII_I_I_I_IIII'| |  
    |  \,III I I I III,/  |  
     \   `~~~~~~~~~~'    /
       \   .       .   /
         \.    ^    ./   
           ^~~~^~~~^"""

name = raw_input("what is your name?")
play()