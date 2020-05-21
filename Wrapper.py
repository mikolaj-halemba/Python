from typing import Callable

def example_function(age: int, timestamp: int) -> str:
    print("7. Age {} and timestamp {}".format(age, timestamp))
    return "HEHEHEHHEHE"


def wrapper(function: Callable) -> Callable:
    print("2. Przygotowuje funkcje wrapujaca")
    def wrapped_function(*args, **kwargs):
        print("6. Wykonuje wrapped_function")
        result = function(*args, **kwargs)
        print("8. Koncze wykonywac wrapped_function z wynikiem:")
        print(result)
        return result
    print("3. Skonczylem przygotowywac funkcje wrapujaca, ktora wynosi:")
    print(wrapped_function)
    return wrapped_function

print("1. Rozpoczynam program")
wrapped_function: Callable = wrapper(example_function)
print("4. Odebralem funkcje wrapujaca:")
print(wrapped_function)

print("5. Rozpoczynam wykonywanie funkcji wrapujacej:")
result = wrapped_function(1, 20)
print("9. Zakonczylem wykonywanie funkcji wrapujacej:")
print('koniec')
print(result)
