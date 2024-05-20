def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def number_to_string(num):
    return str(num)

def opposite(number):
  return number * (-1)

def make_negative( number ):
    if number > 0:
        return number * (-1)
    else:
        return number
    
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
def make_negative( number ):
    if number > 0:
        return number * (-1)
    else:
        return number
    
def remove_char(s):
    return s[1:-1]

def make_negative( number ):
    if number > 0:
        return number * (-1)
    else:
        return number
    
def square_sum(numbers):
    sum = 0
    
    for num in numbers:
        sum = sum + (num * num)
    
    return sum

def double_integer(i):
    return i * 2
