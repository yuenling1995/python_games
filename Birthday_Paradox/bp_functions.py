import datetime
from random import randint



def get_birthdays(num):
	days = [randint(0, 365) for x in range(num)]

	birthdays = []
	start_date = datetime.date(2001, 1, 1)

	for day in days:
		new_date = start_date + datetime.timedelta(days=day)
		#print(new_date)
		new_date_month = new_date.strftime("%b")
		new_date_day = new_date.day 

		new_birthday = new_date_month + " " + str(new_date_day)
		birthdays.append(new_birthday)

	return birthdays 


def find_match_bday(birthdays):
	unique_birthdays = list(set(birthdays))
	duplicates = set()

	if len(birthdays) == len(unique_birthdays):
		return None
	else:
		for birthday in birthdays:
			if birthdays.count(birthday) > 1:
				duplicates.add(birthday)

		duplicates = list(duplicates)
	return duplicates


def run_simulations(num):
	find_match = 0 

	for i in range(100000):
		if i % 10000 == 0:
			print(str(i) + " simulations run...")

		birthdays = get_birthdays(num)
		duplicates = find_match_bday(birthdays)

		if duplicates != None:
			if len(duplicates) >= 1:
				find_match += 1

	print("10,000 simulations run...")
	probability = (find_match / 100000) * 100

	return find_match, probability






