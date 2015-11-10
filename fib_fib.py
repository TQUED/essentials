def find_fib_series(num):
    fib = [0, 1]

    i = int(2)
    
    if int(num) <= 2:
        return fib
    else:
	for a in range(i,int(num)):
	    fib.append[a]
	    a += 1
	find_fib_series(a)
        return fib

a = find_fib_series(3)
print a
