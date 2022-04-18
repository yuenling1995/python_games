import random
import sys
import test_functions as tf


# set up suits
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
suits = [HEARTS, DIAMONDS, SPADES, CLUBS]


# ask bet amount
bet = input("How much do you bet? (1-5000, or QUIT) ")
if bet == "QUIT":
	sys.exit()
else:
	print("Bet: " + bet)


# deal initial cards for both players
dealer, dealer_suits = tf.deal_first_cards(suits)
player, player_suits = tf.deal_first_cards(suits)

print("Dealer: ???")
tf.display_cards( ["BACKSIDE", dealer[1]], dealer_suits)

print("Player: ")
tf.display_cards(player, player_suits)

#compare sums
tf.compare_sums(dealer, player, bet)



while sum(player) < 21:
	if sum(dealer) < 17:	
		# deal new card for dealer
		dealer = tf.deal_card(dealer, dealer_suits)

	# ask player if they want to hit/stand/double down:
	response = input("(H)it, (S)tand, (D)ouble down. ")
	if response.lower() == "h":
		player = tf.deal_card(player, player_suits)
		print("You drew a " + str(player[-1]) + " of " + str(player_suits[-1]) + ".")

	elif response.lower() == "s":
		print("Dealer: ")
		tf.display_cards(dealer, dealer_suits)
		print("Player: ")
		tf.display_cards(player, player_suits)
		# compare sums
		tf.compare_sums(dealer, player, bet)

	elif response.lower() == "d":
		bet = str((int(bet) * 2))
		player = tf.deal_card(player, player_suits)
		print("You drew a " + str(player[-1]) + " of " + str(player_suits[-1]) + ".")

	else:
		print("Wrong response, exit game now.")
		sys.exit()


# compare final sums
print("Dealer: ")
tf.display_cards(dealer, dealer_suits)
print("Player: ")
tf.display_cards(player, player_suits)

tf.compare_sums(dealer, player, bet)


