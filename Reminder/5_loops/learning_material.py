# for loops in a list

fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
  print(fruit)
  print(fruit + ' pie')

student_scores = [150, 142, 185, 120, 184, 24, 59, 60]
sum = 0
max = 0
for score in student_scores:
  sum = sum + score
  if max < score:
    max = score
print(sum)
print(max)

# for loops in a range
# Range function has to be used in conjunction with another function
sum2 = 0
for i in range(1, 101):
  sum2 += i
print(sum2)

for i in range(1, 11, 2):
  print(i)