# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

resVal = {"Rock": 1, "Paper": 2, "Scissors": 3}
play = {"A": "Rock","X": "Rock","B": "Paper", "Y": "Paper","C": "Scissors","Z": "Scissors"}
gain = {"Rock": "Scissors","Scissors": "Paper","Paper": "Rock"}

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win\
trichev = {"X": "lose", "Y": "draw","Z": "win"}
scorePlayer1 = 0
scorePlayer2 = 0

try:
	# with open("2022/2/input.txt") as file:
	# 	lines = file.readlines()
	# 	for line in lines:
	# 		values = line.split(" ")
	# 		player1 = play[values[0]]
	# 		player2 = play[values[1][:1]]
	# 		# print(player1 + "           " + player2)
	# 		if (player1==player2):
	# 			scorePlayer1 += 3
	# 			scorePlayer1 += resVal[player1]

	# 			scorePlayer2 += 3
	# 			scorePlayer2 += resVal[player2]

	# 		else:
	# 			if (gain[player1]==player2):
	# 				scorePlayer1 += resVal[player1]
	# 				scorePlayer1 += 6

	# 				scorePlayer2 += resVal[player2]

	# 			elif (gain[player2]==player1):
	# 				scorePlayer2 += resVal[player2]
	# 				scorePlayer2 += 6

	# 				scorePlayer1 += resVal[player1]

	# 			else:
	# 				scorePlayer1 += 3
	# 				scorePlayer1 += resVal[player1]

	# 				scorePlayer2 += 3
	# 				scorePlayer2 += resVal[player2]


				
	# print("scorePlayer1 : " + str(scorePlayer1))
	# print("scorePlayer2 : " + str(scorePlayer2))

	scorePlayer1 = 0
	scorePlayer2 = 0

	with open("input.txt") as file:
		lines = file.readlines()
		for line in lines:
			# print(line)

			values = line.split(" ")
			player1 = play[values[0]]
			triche2 = trichev[values[1][:1]]

			print(triche2)
			# triche2 = trichev[player2]

			if (triche2=="lose"):
				p2 = gain[player1]
				scorePlayer1 += resVal[player1]
				scorePlayer1 += 6

				scorePlayer2 += resVal[p2]
			elif (triche2=="draw"):
				p2 = player1

				scorePlayer1 += 3
				scorePlayer1 += resVal[player1]

				scorePlayer2 += 3
				scorePlayer2 += resVal[p2]

			elif (triche2=="win"):
				for key, value in gain.items():
					if value==player1:
						p2 = key
						break

				scorePlayer2 += resVal[p2]
				scorePlayer2 += 6

				scorePlayer1 += resVal[player1]


	print("scorePlayer1 : " + str(scorePlayer1))
	print("scorePlayer2 : " + str(scorePlayer2))

except Exception as e:
	print(e)