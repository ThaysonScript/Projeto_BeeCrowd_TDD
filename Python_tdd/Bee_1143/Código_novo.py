def quadrado_cubo(x):
	x = int(input())
	n = 1
	i = 0
	
	while i < x:
		n1 = n
		n2 = n**2
		n3 = n**3
		
		list = [n1, n2, n3]
		
		print(list)
		n = n + 1
		i = i + 1
		
	return list
