
from curses import tigetstr


class Dog:

    def __init__(self, breed , color, age):
        self.breed = breed
        self.color = color
        self.age = age 

    def bark(self, count):
        print("woof"*count)
        
    def eat(self,food):
        print(f"dog eats{food}")
    
class Shape:
    def __init__(self , name , sides):
        self.name = name 
        self.sides = sides 

    def perimeter (self, size = 20):
        return self.sides*size

#string notation of the object
    def __str__(self):
        return f"{self.name} has {self.sides} sides "

#this line checks if the file you run is the file or not 
if __name__ == "__main__":
    tommy = Dog('steet Dog','brown',3)
    tiger = Dog('bulldog','black',2)

    print ('object', tommy)
    print('object', tiger)

    
    print('tommy\'s breed',tommy.breed)
    print('tommy\'s age', tommy.age)





     sqr = Shape('square',4)
     tri = Shape('triangle',3)
     ptn = Shape('pentagon'5)

     print('object=>',sqr)
     print('object=>',tri)
     print('object=>',ptn)
    
    print('square perimater',sqr.perimeter)
    print('triangle perimeter',tri.perimeter)
    print('pentagon',ptn.perimeter)
    




    
