def is_prime(n):
	prime = True
	if n == 2:
		return prime
	else:
		for i in range(2,n):
			if n%i == 0:
				prime = False
				break
	return prime

#_main_
list = []
for i in range(2,100):
	x = is_prime(i)
	if x == True:
		list.append(i)
print(list)

