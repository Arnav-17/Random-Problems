import matplotlib.pyplot as plt
n = int(input("Enter generation number\n"))

def func(p, w11, w12, w22):
	a = [p]
	b = [0]
	c = [(1-p)**2]
	d = [2*p*(1-p)]
	for i in range(1, n):
		p += p*(1-p)*(p*(w11-w12)-(1-p)*(w22-w12))/(p**2*w11+2*p*(1-p)*w12+(1-p)**2*w22)
		a.append(p)
		b.append(i)
	plt.plot(b, a)
	plt.xlabel('No. of Generations')
	plt.ylabel('Frequency of p')
	plt.show()

	
func(0.4, 1, 0.5, 0.8)