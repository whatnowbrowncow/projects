def rps():
	from random import randint
	print "ROCK - PAPER - Scissors"
	game = 1
	compscore = 0
	playerscore = 0
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
			retry()
		game = game + 1
	print "The final score is", "me", compscore, "you", playerscore

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
		print "Paper beats Rock, You Win!"
		rplayerscore = rplayerscore + 1
	elif compchoice == "Rock" and playerchoice == "Scissors":
		print "Rock beats Scissors, I Win!"
		rcompscore = rcompscore + 1
	elif compchoice == "Paper" and playerchoice == "Scissors":
		print "Scissors beats Paper, You Win!"
		rplayerscore = rplayerscore + 1
	elif compchoice == "Paper" and playerchoice == "Rock":
		print "Paper beats Rock, I Win!"
		rcompscore = rcompscore + 1
	elif compchoice == "Scissors" and playerchoice == "Rock":
		print "Scissors beats Rock, You Win!"
		rplayerscore = rplayerscore + 1
	elif compchoice == "Scissors" and playerchoice == "Paper":
		print "Scissors beats Paper, I Win!"
		rcompscore = rcompscore + 1
	else:
		print "we Both picked the same, it's a draw!"
		retry()
	print rcompscore
	print rplayerscore

rps()