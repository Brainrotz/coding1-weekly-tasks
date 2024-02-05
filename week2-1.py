
a = 5
b = 50
c = 15

sum = 0

for i in range(a, b):
	if i % c == 0:
		sum += i

print(sum)