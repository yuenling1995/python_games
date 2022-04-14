import random
import bagels_functions as bf 



def run_game():

	print("Bagels, a deductive logic game.\n")
	print("By Al Sweigart al@inventwithpython.com\n")
	print("I am thinking of a 3-digit number. Try to guess what it is.\n")
	print("Here are some clues:\n")
	print("When I say:         " + "That means:\n")
	print("Pico         " + "One digit is correct but in the wrong position.\n")
	print("Fermi        " + "One digit is correct and in the right position.\n")
	print("Bagels       " + "No digit is correct.\n")
	print("I have thought up a number.\n")
	print("  You have 10 guesses to get it.\n")

	num_digit = 3
	num_guess = 10

	# generate a random 3-digit number as answer
	answer = bf.get_answer(num_digit)
	print(answer)

	while True:
		round = 1

		while round <= num_guess:
			guess = input("Guess " + str(round) + ": ")

			if guess == answer:
				print("You get it!")
				break
			else:
				bf.test_guess(guess, answer)
				round += 1

		print("The answer is " + answer + ".\n")
		play_next = input("Do you want to play again? (y/n) ")
		if play_next == 'y':
			answer = bf.get_answer(num_digit)
			print(answer) 
			bf.reset_round(round)
		else:
			break



run_game()


