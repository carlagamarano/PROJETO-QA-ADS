#Teste para validar se o número é par

def is_even(number):
    return number % 2 == 0


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True 
    assert is_even(-2) == True  
    assert is_even(-3) == False 
