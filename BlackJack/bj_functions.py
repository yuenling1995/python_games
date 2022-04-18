import random
import sys



def deal_first_cards(suits):
	cards = [random.randint(1, 13) for x in range(2)]
	cards_suits = [random.choice(suits) for x in range(2)]

	return cards, cards_suits


def change_values(cards):
	new_cards = []
	for card in cards:
		if card == 11:
			card = 10
			new_cards.append(card)
		elif card == 12:
			card = 10
			new_cards.append(card)
		elif card == 13:
			card = 10
			new_cards.append(card)
		else:
			new_cards.append(card)
	return new_cards


def compare_sums(dealer, player, bet):
	dealer = change_values(dealer)
	player = change_values(player)

	if sum(dealer) == 21:
		print("BlackJack! Dealer wins!")
		sys.exit()
	elif sum(player) == 21:
		print("BlackJack! Player wins " + str(bet) + "!")
		sys.exit()
	elif sum(dealer) > 21 or sum(player) > 21:
		if sum(dealer) == sum(player):
			print("There is a tie!")
			sys.exit()
		elif sum(dealer) > 21:
			print("Dealer went over, player wins " + str(bet) + "!")
			sys.exit()
		elif sum(player) > 21:
			print("Player went over, dealer wins!")
			sys.exit()


def deal_card(cards, suits):
	new_card = random.randint(1, 13)
	new_suit = random.choice(suits)
	cards.append(new_card)
	suits.append(new_suit)
	return cards


def display_cards(cards, suits):
	rows = ["", "", "", ""]
	cards_copy = switch_number(cards)
	for i, card in enumerate(cards_copy):
		rows[0] += " ___ "
		if card == "BACKSIDE":
			rows[1] += "|## |"
			rows[2] += "|###|"
			rows[3] += "|_##|"
		else:
			rows[1] += "|{}  |".format(card)
			rows[2] += "| {} |".format(suits[i])
			rows[3] += "|__{}|".format(card)

	for row in rows:
		print(row)


def switch_number(cards):
	cards_copy = []
	for card in cards:
		if card == 11:
			card = "J"
			cards_copy.append(card)
		elif card == 12:
			card = "Q"
			cards_copy.append(card)
		elif card == 13:
			card = "K"
			cards_copy.append(card)
		else:
			cards_copy.append(card)
	return cards_copy














