#Generators are the real functions in python 
#That can be used to generates a sequence of values 
#Instead of returning the values from a function once 
# and then we can use the next() function to get the next value 

from re import A


def cube(limit):
    for i in range (1,limit):
        yield i**3

def fib(limit):
    a,b = 0,1
    for i in range (limit):
        yield a 
        a,b = b,a+b

#ex call 
for c in cube (10):
    print (c)

for f in fib (15):
    print (f, end='|')

#WAP TO GENERATE THE LIST OF EVEN SQUARE USING GENEARATORS 
#WAP TO GENERATE A LIST OF ACRONYMNS FROM A LIST OF WORDS USING GENERATORS & * ARGS


def sqr(limit):
    for i in range (1,limit):
        if i%2==0:
         yield i **2

def fib (limit):
    a,b = 0,1
    for i in range (limit):
        yield a
        a,b = b,a+b 

#ex call 
for s in sqr (10):
    print(s)



