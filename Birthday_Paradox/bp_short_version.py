from random import randint
import datetime




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
	num_match = 0

	for i in range(10000):
		birthdays = get_birthdays(num)
		duplicates = find_match_bday(birthdays)

		if duplicates != None :
			if len(duplicates) >= 1:
				num_match += 1


	probability = (num_match/10000) * 100
	return probability


probability = run_simulations(50)
print(probability)





