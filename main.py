# 1. print a numbers from 1 to 10 using a range() function
#    hint: in range(start, stop, step) function:
#    - start is inclusive 
#    - stop is exclusive 
#    - step is optional  
# 2. print a number from 10 to 1 using a range() function
#    hint: you can pass -1 in steps argument


# 1. print a numbers from 1 to 10 using a range() function
#note: print() here uses multiple arguments to format
#print() function concatnates both args string and int and also adds a single space between them.
for number in range(1,11):
  print('A number:', number)
print('--------------******--------------\n')


# 2. print a number from 10 to 1 using a range() function
for number in range(10,0,-1):
  print('A number:', number)
print('--------------******--------------\n')
