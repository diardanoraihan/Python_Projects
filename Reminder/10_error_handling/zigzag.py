'''
This small program will create a back-and-forth, zigzag pattern until the user stops
it by pressing the stop button or pressing CRTL + C.
When you run the program, the output will look something like this:
    ********
   ********
  ********
 ********
********
 ********
  ********
   ********
    ********
'''
import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
  while(True):
    print(' ' * indent, end = '')
    print('********')
    time.sleep(0.1) # Pause for 1/10 of a second
    
    if indentIncreasing:
      # increase the number of spaces
      indent += 1
      if indent == 20:
        # change direction
        indentIncreasing = False
    
    else:
      # decrease the number of spaces
      indent -= 1
      if indent == 0:
        indentIncreasing = True

# When the user presses CTRL-C while the program is running, Python raises the KeyboardInterrupt exception.
except KeyboardInterrupt:
  sys.exit()

'''
If there is no try-except statement to catch this exception, the program crashes with an ugly error message. 
However, for our program, we want it to cleanly handle the KeyboardInterrupt exception by calling sys.exit().

If the user presses CTRL-C at any point that the program execution is in the try block, 
the KeyboardInterrrupt exception is raised and handled by this except statement. 

The program execution moves inside the except block, which runs sys.exit() and quits the program. 
This way, even though the main program loop is an infinite loop, the user has a way to shut down the program.
'''