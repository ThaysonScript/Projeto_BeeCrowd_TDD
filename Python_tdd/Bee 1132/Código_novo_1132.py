def multiplos_13(num):
    x = int(input())
    y = int(input())
    
      #13  #10
    if x >= y:
        n1 = y #10
        n2 = x #13
        
    if x <= y:
        n1 = x
        n2 = y
        
    soma = 0
        
         #10    #13
    while n1 <= n2:
          #10
        if n1%13 != 0:
              
        #exemplo de saída:
              	
       	#soma = 0 + 10    10
       	#soma = 10 + 11    11
       	#soma = 21 + 12    12
       	#soma = 33        
       	
             #0     0   + 10
            soma = soma + n1 #10
            #10 + 1
        n1 = n1 + 1
            
    print(f'{soma}')
    return soma
