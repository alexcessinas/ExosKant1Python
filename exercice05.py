def is_number_correct(number):
    # Votre code ici
    result: (bool, int)
    if number > 9 and number < 21:
        result = (True, 0)
    else:
        if number < 10: 
            result = (False, 10 - number)
        elif number > 20: 
            result = (False, 20 - number)
    return result

def run():
    assert is_number_correct(0) == (False, 10)
    assert is_number_correct(10) == (True, 0)
    assert is_number_correct(20) == (True, 0)
    assert is_number_correct(21) == (False, -1)
    assert is_number_correct(50) == (False, -30)
    assert is_number_correct(15) == (True, 0)