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
		print "CONGRATULATIONS %s, You have won this round and get to progress to the final round......"%(name)
		print "!!!!!!!!!!!!!!!!!THE DEATH MATCH!!!!!!!!!!!!!!"
		print """
			     .xm*f""??T?@hc.
                          z@"` '~((!!!!!!!?*m.
                        z$$$K   ~~(/!!!!!!!!!Mh
                      .f` "#$k'`~~\!!!!!!!!!!!MMc
                     :"     f*! ~:~(!!!!!!!!!!XHMk
                     f      " %n:~(!!!!!!!!!!!HMMM.
                    d          X~!~(!!!!!!!X!X!SMMR
                    M :   x::  :~~!>!!!!!!MNWXMMM@R
 n                  E ' *  ueeeeiu(!!XUWWWWWXMRHMMM>                :.
 E%                 E  8 .$$$$$$$$K!!$$$$$$$$&M$RMM>               :"5
z  %                3  $ 4$$$$$$$$!~!*$$$$$$$$!$MM$               :" `
K   ":              ?> # '#$$$$$#~!!!!TR$$$$$R?@MME              z   R
?     %.             5     ^""~~~:XW!!!!T?T!XSMMM~            :^    J
 ".    ^s             ?.       ~~d$X$NX!!!!!!M!MM             f     :~
  '+.    #L            *c:.    .~"?!??!!!!!XX@M@~           z"    .*
    '+     %L           #c`"!+~~~!/!!!!!!@*TM8M           z"    .~
      ":    '%.         'C*X  .!~!~!!!!!X!!!@RF         .#     +
        ":    ^%.        9-MX!X!!X~H!!M!N!X$MM        .#`    +"
          #:    "n       'L'!~M~)H!M!XX!$!XMXF      .+`   .z"
            #:    ":      R *H$@@$H$*@$@$@$%M~     z`    +"
              %:   `*L    'k' M!~M~X!!$!@H!tF    z"    z"
                *:   ^*L   "k ~~~!~!!!!!M!X*   z*   .+"
                  "s   ^*L  '%:.~~~:!!!!XH"  z#   .*"
                    #s   ^%L  ^"#4@UU@##"  z#   .*"
                      #s   ^%L           z#   .r"
                        #s   ^%.       u#   .r"
                          #i   '%.   u#   .@"
                            #s   ^%u#   .@"
                              #s x#   .*"
                               x#`  .@%.
                             x#`  .d"  "%.
                           xf~  .r" #s   "%.
                     u   x*`  .r"     #s   "%.  x.
                     %Mu*`  x*"         #m.  "%zX"
                     :R(h x*              "h..*dN.
                   u@NM5e#>                 7?dMRMh.
                 z$@M@$#"#"                 *""*@MM$hL
               u@@MM8*                          "*$M@Mh.
             z$RRM8F"                             "N8@M$bL
            5`RM$#                                  'R88f)R
            'h.$"                                     #$x*"""



rps()