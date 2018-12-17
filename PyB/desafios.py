"""x*(x-1)*(x-2)...*1"""

def fatorial(x):
	r = 1
	for i in range(1,x+1):
		r *= i
	return r

# print(fatorial(0))

def fatorial_rec(x):
	if x == 0:
		return 1
	return(x*fatorial_rec(x-1))

# print(fatorial_rec(997))

def primo(x):
	if x == 1 or x == 2:
		return True
	if x % 2 == 0:
		return False
	i = 3
	while i*i <= (x):
		if x%i == 0:
			return False
		i += 2
	return True

print(primo(53))