n = 7
guessed = False
guesses = []
while not guessed:
	guess = int(input("Guess a number: "))
	if len(guesses) == 0 or guess != guesses[len(guesses) - 1]:
		guesses.append(guess)

	if guess > n:
		print("Too high")
	elif guess < n:
		print("Too low")
	else:
		print("Correct!")
		# print("Guessed", count, "times")
		print("Guessed", len(guesses), "times")
		guessed = True9