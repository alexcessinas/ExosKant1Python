def factorial(num):
    # Votre code ici
    if num < 0: 
        fact = 1
        num = num * -1
        while(num > 1):
            fact *= num 
            num -= 1
        return fact * -1

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320