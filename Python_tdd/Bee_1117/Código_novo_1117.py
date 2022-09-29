def validar_nota(num):
    media = total = i = 0
    while i != 2:
        n = float(input())
        if n >= 0 and n <= 10:
            media = (n/2) + media
            i += 1
        else:
            print('nota invalida')
    print(f'media = {media:.2f}')
    return media
