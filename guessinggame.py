import random as rnd

yourNumber = 0
yourInput      = ""

# Solicit input until it is correct.
while(not(yourNumber in range (1,11))):
	try:
		yourInput  = input("\nEnter a number between 1 & 10 and I'll try to guess it ---> ")
		yourNumber = int (yourInput)
		
	except:
		print (f"\n'{yourInput}' is not a number...\n\n")

# Make our guess and evaluate.
myGuess = rnd.randint(1, 10)

print (f"\nYour number is {yourNumber} and my guess is {myGuess}...  ")

if (myGuess == yourNumber):
	print ("I guessed it!\n")
	
else:
	print ("I am wrong.\n")
