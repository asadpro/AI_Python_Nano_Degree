# String formate
# for x in range(1, 11):
#     # Below 2,3,4 are the spaces to be added
#     print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))

# Doing the same table of squares above manually
# for x in range(1, 11):
#     print(f"{str(x).rjust(2)} {str(x*x).rjust(4)} {str(x*x*x).rjust(6)}")

# name = "asad"
# print(name.center(10, "🍡"))
# Both of below method will fill the left side with zeroes
# print(name.zfill(10))
# print(name.rjust(10, "0"))


# 🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓 Classes 🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓
# class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def display(self):
#         print("Name of your cat: {}\nColor of Cat: {}".format(self.name, self.color))


# class Shefered(Dog):
#     def speed(self, speed):
#         self.speed = speed
#         print(f"Shefered dog have speed of: {speed}mph")


# d = Dog("Beauty", "White")
# s = Shefered(name="Shefered", color="Yellow")
# s.speed(speed=34)
# d.display()

# # To check whether 'Shefered' is subclass of 'Dog' class
# print(issubclass(Shefered, Dog))
# # To check whether s is an instance of class Dog
"""
object
  |
  +-- type
       |
       +-- bool
       +-- int
       +-- float
       +-- complex
       |
       +-- str
       |    |
       |    +-- bytes
       |
       +-- list
       |    |
       |    +-- tuple
       |
       +-- set
       |    |
       |    +-- frozenset
       |
       +-- dict
       |
       +-- range
       |
       +-- function
       |    |
       |    +-- method
       |
       +-- module
       |
       +-- ...

This hierarchy shows the relationships between the built-in 
classes in Python, with the object class at the top and the 
other classes derived from it. The classes that are indented 
under a particular class are its subclasses. For example, the
bool class is a subclass of the int class, which is a subclass 
of the object class.
"""

# print(isinstance(s, Dog))
# print(issubclass(type, object))
# print(issubclass(bytes, str))
# print(issubclass(tuple, list))
# print(issubclass(frozenset, type))
# print(issubclass(type, object))


"""
For loop works using two main functions 'iter()', 'next()' for
statement call the iter() method on the container (list, tuple, set)
which returns us the iterator (contain a stream of data) no this 
iterator define the the next() method which return a single 
element from this list one by one. if there is no element then
next() function return the StopIteration Exception.
"""
# name = "asad"
# iterate = iter(name)  # this will return str_iterator if list then list_iterator
# for i in range(len(name)):
#     print(next(iterate) )


# Generator are special kind of function in python that produces a sequence
# of values, one at a time, when you iterate over it.
# To create a generator you use the 'yield' keyword instead of return


# def func(sequence):
#     for i in range(len(sequence)):
#         yield i * i
#         print("Single Iteration")


# for singleSquare in func([1, 2, 3, 4, 5, 6]):
#     print(singleSquare)
