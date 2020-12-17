'''
Time library allows us to measure how fast
our algorithm is running.

Some functions we explore in time library:
- clock
- sleep
- uniform
- choice
- shuffle
'''
import time

# measure how fast our algorithm is running.
currentTime = time.clock()
print("hello")
pastTime = time.clock()
print("Time passed: ", pastTime - currentTime)

print("1")
# Make your time sleep (break) in a certain amount of time. In this case, 3 seconds
time.sleep(3)
print("2")

for i in range(1,11):
    print(i)
    time.sleep(1)

