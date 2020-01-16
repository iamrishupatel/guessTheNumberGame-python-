###THIS A SIMPLE NUMBER GUESSING GAME###
### Created by Rishu Patel on july 3rd 2019
### Added chances in hard an god modes on july 4th

print("\n\t\t\t\t##This is a Number Guessing Game created by Rishu Patel##")
print("\t\t\t\t\tHint_ All numbers are less than 10000\n")
print("Please Select a Level")
print("1: Normal (unlimited chances)\n2: Moderate (unlimited chances)\n3: Hard (you will get only 20 chances to guess a number)\n4:God Mode (you will get only 10 chances to guess a number)\n ")

#now user will select levels
level_select = int(input("Select your level:- "))

#depending on the level selection i have taken different lists


normals = (152,3620,145,478,285,1023,2722,975,356,464)
moderates = (1549,3560,3659,4895,9871,3496,9774,4785,6985,3256)
hards = (4263,3000,1245,8924,9873,2546,2893,7853,9854,5669)
gods = (4692,9846,6479,7823,7891,9875,2366,259,848,1)


normal_guess = 0
moderate_guess = 0
hard_guess = 0
god_guess = 0


#if user selects the level 1 
if level_select == 1:
	print("You are in normal level!")
	print("I am thinking of a number try to guess that number!")	
	for normal in normals:
		while normal_guess != normal:
			normal_guess = int(input("Try to guess the Number: "))
			if normal_guess > normal: 
				if  normal_guess > (normal + 2000):
					print("Its much smaller!")
					print()
				else:
					print("Its bit smaller!")
					print()
			elif normal_guess < normal:
				if normal_guess < (normal - 2000):
					print("Its much bigger!")
					print()
				else:
					print("Its bit bigger!")
					print()
			else:
				print("Congratulation you guessed it right!!!")	
				print()
		option1 = input("Do you want to play again?(y/n): ")
		if option1 == 'n':
			break
#if user selects the level 2					
elif level_select == 2:
	print("You are in moderate level!")
	print("I am thinking of a number try to guess that number!")
	for moderate in moderates:
		while moderate_guess != moderate:
			moderate_guess = int(input("Try to guess the Number: "))
			if moderate_guess > moderate: 
				if  moderate_guess > (moderate + 3500):
					print("Its much smaller!")
					print()
				else:
					print("Its bit smaller!")
					print()
			elif moderate_guess < moderate:
				if moderate_guess < (moderate - 3500):
					print("Its much bigger!")
					print()
				else:
					print("Its bit bigger!")
					print()
			else:
				print("Congratulation you guessed it right!!!")	
				print()
		option2 = input("Do you want to play again?(y/n): ")
		if option2 == 'n':
			break
#if user selects the level 3			
elif level_select == 3:
	print("You are in hard level!")
	print("I am thinking of a number try to guess that number!")
	for hard in hards:
		i = 0
		while hard_guess != hard and i < 20:
			hard_guess = int(input("Try to guess the Number: "))
			i += 1
			if hard_guess > hard: 
				if  hard_guess > (hard + 5000):
					print("Its much smaller!")
					print("You have",20 - i,"chances left")
					print()
				else:
					print("Its bit smaller!")
					print("You have",20 - i,"chances left")
					print()
			elif hard_guess < hard:
				if hard_guess < (hard - 5000):
					print("Its much bigger!")
					print("You have",20 - i,"chances left")
					print()
				else:
					print("Its bit bigger!")
					print("You have",20 - i,"chances left")
					print()
			else:
				print("Congatulation you guessed it right!!!")
				print()
		option3 = input("Do you want to play again?(y/n): ")
		if option3 == 'n':
			break
		else:
			continue
#if user selects the level 4
elif level_select == 4:
	print("You are in god level!")
	print("I am thinking of a number try to guess that number!")
	for god in gods:
		i = 0
		while god_guess != god and i < 10:
			god_guess = int(input("Try to guess the Number: "))
			i +=1 
			if god_guess > god: 
				if  god_guess > (god + 5000):
					print("Its much smaller!")
					print("You have",10 - i,"chances left")
					print()
				else:
					print("Its bit smaller!")
					print("You have",10 - i,"chances left")
					print()
			elif god_guess < god:
				if god_guess < (god - 5000):
					print("Its much bigger!")
					print("You have",10 - i,"chances left")
					print()
				else:
					print("Its bit bigger!")
					print("You have",10 - i,"chances left")
					print()
			else:
				print("Congratulation you guessed it right!!!")	
				print()
		option4 = input("Do you want to play again?(y/n): ")
		if option4 == 'n':
			break
		else:
			continue

else:
	print("Please select a valid level")
