def abc(x):
	return x**2+2*x+3
t=int(input())
print(abc(abc(abc(t)+t)+abc(abc(t))))
