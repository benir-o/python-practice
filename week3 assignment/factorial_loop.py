def get_factorial(number):
    digit=1
    for i in range(1,number+1):
        digit*=i
    return digit
print(get_factorial(3))
