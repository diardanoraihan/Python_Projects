"""
Title:
Homework Assignment #5: Basic Loops
"""
fizz,buzz,fizzbuzz,prime = [],[],[],[]

for i in range(1,101):
    if i%3==0 and i%5!=0 and i!=3:
        print('Fizz')
        fizz.append(i)
    elif i%3!=0 and i%5==0 and i!=5:
        print('Buzz')
        buzz.append(i)
    elif i%5==0 and i%3==0:
        print('FizzBuzz')
        fizzbuzz.append(i)
    elif i==2 or i==3 or i==5 or i==7:
        print('Prime')
        prime.append(i)
    elif i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i!=1:
        print('Prime')
        prime.append(i)
    else:
        print(i)

# For debugging purpose
# print('Fizz: {}'.format(fizz))
# print('Buzz: {}'.format(buzz))
# print('FizzBuzz: {}'.format(fizzbuzz))
# print('Prime: {}'.format(prime))
