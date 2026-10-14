num = int(input("digite um numero para verificarmos se é primo ou não: "))

def ePrimo():
    if num <= 1:
        return False
    
    if num == 2:
        return True
        
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True 

if ePrimo() == True:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo!")