number_input=input("Enter the number: ")

def summing_the_number(number):
    numlist=list(map(int,number))
    accumulator=0
    for item in numlist:
        accumulator+=item
    return accumulator
print(summing_the_number(number_input))
#Finished



