# Loops
## For vs While Loops
### For Loop
- Really great when you want to iterate over something and you need to do something with each thing that you are iterating over.
- Example:
```
fruits = ['Apple', 'Banana', 'Orange']
for fruit in fruits:
  print(fruit)

for i in range(1, 6):
  print(i)
```
### While Loop
- Use while loop when you don't really care:
  - what number in a sequence you are in, 
  - which item you are iterating through in a list
- You just want to simply carry out some sort of functionality many times until some sort of condition that you set.
- While loops are a bit more dangerous since it can generate infinite loop: sort of condition that actually never becomes false!!!
```
while 5>3:
  print('Yes') # this will print "Yes" until the end of time!
```