import matplotlib.pyplot as plt
l = int(input("Enter generation number\n"))

def func(P, p, m, n):
	a = [p]
	b = [0]
	c = [(1-p)**2]
	d = [2*p*(1-p)]
	for i in range(1, l):
		p += (m - m*p - n*p)/(P+m+n)
		x = 1 - p
		a.append(p)
		b.append(i)
		c.append(x)
	plt.plot(b, a)
	plt.plot(b, c)
	plt.show()
	return p

	
print(func(1000, 0.8, 30, 50))