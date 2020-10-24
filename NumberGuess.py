import random 

#generate target within defined range
target = random.randrange(1,101,1) 


def numberGuess():
	''' asks for int value between defined range. Checks if value is int '''
	while True :
		value = input("Enter an integer between 1 and 100\n") 
		try:
			value = int(value)
			return value
		
		except ValueError:
			print("Value must be an integer\n")

#get first guess
value = numberGuess()

#check if number is too low or too 
while True: 
	
	if value > target:
		print ("Too High")
		value = numberGuess()

	elif int(value) < target: 
		print("Too Low")
		value = numberGuess()

	else: 
		print("Pefect")
		break
	

