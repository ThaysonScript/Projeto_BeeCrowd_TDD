x = int(input())
y= int(input())

if x > y:
    n1 = y
    n2 = x
if x <= y:
    n1 = x
    n2 = y
   
soma = 0

while n1 <= n2:
    if n1 % 13 != 0:
        soma = soma + n1
    n1 = n1 + 1
print('{}'.format(soma))
