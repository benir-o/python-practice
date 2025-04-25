# Data Structures and Algorithms Assignment
> Omenda Benir Odeny - 192559
## 1. Summing all elements in a list
Here we create a list of numbers. An example is [1 ,2 ,3]
We then iterate over the list from the item in position 0 to the item in position 3, while updating our sum variable.

### Summation code
``` python
def find_sum(mylist):
    summation=0
    for i in mylist:
        summation= summation + i
    return summation
mylist=[1,2,3,4,5]
print(find_sum(mylist))
```
## 2. Checking whether a number is even or odd
Logic: If a number is even, when we divide it by 2 the remainder is 0, otherwise we get an odd number.
Here I create a simple function that prints out "odd" or "even" according to the interpratation of the if-else logic statement.

### Number-type determining code
``` python
def check(number):
    if number%2==0:
        print("even!")
    else:
        print("odd!")

check(9)
```
## 3. Computing the factorial using a loop
To compute the factorial using a loop, we utilize the range function in python. Automatically, our range will start at 1 and not 0 since we are not using recursion.
We allow the user to input a certain value, hence the range will be from 1 to that value plus an extra 1, which becomes our upper boundary. 
This means that the upper boundary is not included while we iterate.
### Strategy
We set a variable to be equal to 1. 
During for loop iteration, we multiply that variable by 1, then 2, then 3, upto the specified number.
The variable's value then re-updates in memory according to the arithmetic operation that we perform.

### Factorial for-loop code
``` python
def get_factorial(number):
    digit=1
    for i in range(1,number+1):
        digit*=i
    return digit
print(get_factorial(3))

```

## 4. Reversing a string
I created an input system that allows the user to input a string. We then split the string to individual characters using the list () method. 
for a name like nir, we get a list with items as follows: ['n','i','r']. 

Here we iterate from position 0 to 2. But there's a catch. We can also set a variable to -1, which is the position of the last element in our list.
At position 0, we print the item at position -1. At position 1, we print the item at position -2 and at position 2 we print the item at position -3.
while we iterate through our list from 0 to 2, we set one variable to be -1 and then decrement it by 1 at the end of each iteration, the result is a string in reverse order.

### Code for string reversal
``` python

word=input("Enter word: ")

def word_reversal(word_detail):
    word_character_list=list(word_detail)
    j=-1
    for _ in word_character_list:
        print(word_character_list[j],end="")
        j-=1

word_reversal(word)
```
## 5. Finding the factorial using recursion
We set up a function that calls itself. The base case is hit when our digit is 0. At 0, we return the value 1 since the factorial of 0 is 1.
if not we multiply that number by the factorial of the digit that is less than that number by 1, as follows:

### Recursive factorial 
```python
def find_factorial(number):
    if number==0:
        return 1
    else:
        return number*find_factorial(number-1)

print(find_factorial(3))
```
A pop operation occurs after the base case is hit.
## 6. Summing the digits of a number
Finally, we allow the user to enter a number, convert it into a list of integers using the map method which returns integer values. 
This is then parsed into the list method which puts the integers in list form.
We then design an accumulator variable with an intial value of 0 and iterate over from position 0 up to the last position.
During iteration, we update the accumulator variable to be equal to the digit at the nth positiion plus its initial value

### Summation code
``` python
number_input=input("Enter the number: ")

def summing_the_number(number):
    numlist=list(map(int,number))
    accumulator=0
    for item in numlist:
        accumulator+=item
    return accumulator
print(summing_the_number(number_input))
```

# Author
> Omenda Benir Odeny
