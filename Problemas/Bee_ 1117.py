media = 0
total = 0

i = 0

while i != 2:
    n = float(input())
    
    if n >= 0 and n <= 10:
        media = n / 2 + media
        i = i + 1
    else:
        print('nota invalida')
    

print('media = {:.2f}'.format(media))
