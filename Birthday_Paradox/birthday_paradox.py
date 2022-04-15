import datetime, random
import bp_functions as bf


def main():

	print("""
Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, 
the odds that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising results.
	""")


	# get a list of random birthdays based on input
	num = input("How many birthdays shall I generate? (Max 100) ")
	if 0 < int(num) <= 100:
		num = int(num)

	birthdays = bf.get_birthdays(num)
	print("There are " + str(len(birthdays)) + " birthdays:")

	# find if there's match birthdays & display results
	duplicates = bf.find_match_bday(birthdays)

	if duplicates != 0:
		print("In this simulation, \n")
		print("Multiple people share the same birthdays on:")
		for dup in duplicates:
			print(dup)
	else:
		print("There is no matching birthdays!")
	

	# run through 100,000 simulations
	print("Generating " + str(len(birthdays)) + " random birthdays 100,000 times...")
	input("Press Enter to begin...")

	# run the match loop 100,000 times
	print("Let's run another 100,000 simulations.")

	# find the probability of sharing same birthdays in 100,000 simulations
	find_match = bf.run_simulations(num)
	print(find_match)
	probability = bf.find_probability(find_match)

	# display simulation results
	print("Out of 100,000 simulations of " + str(len(birthdays)) + " people, there was a")
	print("matching birthday in that group " + str(find_match) + " times. This means")
	print("that " + str(len(birthdays)) + " people have a " + str(probability) + " % chance of" )
	print("having a matching birthday in their group.")
	print("That's probably more than you would think!")
  
  
  
