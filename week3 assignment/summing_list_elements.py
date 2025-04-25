def find_sum(mylist):
    summation=0
    for i in mylist:
        summation= summation + i
    return summation
mylist=[1,2,3,4,5]
print(find_sum(mylist))