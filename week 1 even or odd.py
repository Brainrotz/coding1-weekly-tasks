# Write a program that outputs “even” if a number is even and “odd” if a number is odd.

try:
	n = float(input("input a number: "))
	if n % 2 == 0:
		print("even")
	elif n % 2 == 1:
		print("odd")
	else:
		print("Not a valid integer")

except Exception as e:
	print(e)
	# print("Error trying to determine number is even or odd")


