import random


def get_answer(num_digit):
	digits = [str(x) for x in range(10)]
	random.shuffle(digits)

	answer = ''
	for i in range(num_digit):
		answer += digits[i]
	return answer


def test_guess(guess, answer):
	for i in range(len(guess)):
		if guess[i] == answer[i]:
			print("Fermi")
		elif guess[i] in answer:
			print("Pico")
		else:
			print("Bagels")

def reset_round(round):
	round = 1


