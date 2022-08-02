#WAP TO GENERATE THE LIST OF EVEN SQUARE USING GENEARATORS 
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
