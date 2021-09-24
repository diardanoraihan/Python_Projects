'''
Decorator in Python
- We create a function to modify the original function that we want to keep intact.
- In the example, we create a function 'smart_div' that will return a function 'inner' that will also 
return a function to modify the input function as a parameter in 'smart_div'

'''
# decorator syntax
def smart_div(func):
    
    def inner(a,b):
        if a>b:
            a,b = b,a
        
        return func(a,b)
    
    return inner


# divNew = smart_div(div)
# divNew(4,2)

@smart_div
def div(a,b):
    print(a/b)

div(4,2) # this will return 0.5 (NOT 2)

'''Above code is equivalent to ->

def div(a,b):
    print(a/b)
    
div = smart_div(div)
'''



    




