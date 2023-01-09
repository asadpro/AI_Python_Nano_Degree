# # Write your code here
# def findflower(nameofperson, flowersname):
#     for key in flowersname:
#         if nameofperson[0].capitalize() == key:
#             return flowersname[key]


# # HINT: create a dictionary from flowers.txt
# flower = {}
# with open("flowers.txt") as file:
#     lines = file.readlines()
#     for i in range(len(lines)):
#         flower[lines[i].split(":")[0]] = lines[i].split(":")[1].removesuffix("\n")

# # HINT: create a function to ask for user's first and last name
# def askuser():
#     return input("Enter your first name: ") + input("Enter your last name only: ")


# # print the desired output
# print(findflower(askuser(), flower))

# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# import tkinter as tk

# window = tk.Tk()

# Printing all the ascii charcters
# chars = ""
# for i in range(128):
#     chars += chr(i)

# print(chars[65])
# unicode_char = ""
# for i in range(1000):
#     unicode_code_point = 0x0 + i
#     unicode_char += chr(unicode_code_point)

# print(unicode_char, " ")

# Removing duplicate through set method
# new_chars = set(chars)
# print(new_chars)
# print(len(new_chars))

# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# To continue the logical line we need to insert backslash for it's continuation
# para = "Two or more physical lines may be joined into logical lines using\
# backslash characters (\), as follows: when a physical line ends in a \
# backslash that is not part of a string literal or comment, it is joined\
# with the following forming a single logical line, deleting the backslash\
# and the following end-of-line character. For example:"
# print(para)

# How tokens are generated using NEWLINE, INDENT, DEDENT with the help of stack

#  def perm(l):                       # error: first line indented
# for i in range(len(l)):             # error: not indented
#     s = l[:i] + l[i+1:]
#         p = perm(l[:i] + l[i+1:])   # error: unexpected indent
#         for x in p:
#                 r.append(l[i:i+1] + x)
#             return r

# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# The following string will read as bytes data
# raw = rb"\Urawstring\u"
# rawbackslash = "\\n"

# fname = "asad"
# lname = "pro"
# print(f"your full name: {fname +'' +' '+ lname }")
# print(rawbackslash)
# escape = "--\a--\b--\f--\n--\r--\t--\v--\o\0oo"
# print(escape)
# print(type(raw))

# name = "Asad"
# print(f"My name is {repr(name)}")

# from datetime import datetime

# today = datetime(year=2022, month=12, day=14, hour=12, minute=59, second=30)
# print(f"{today:  %B %d %Y}")  # using date format specifier
# line = "The mill's closed"
# print(f"{line = }")
# longinteger = 109_432_353
# print(longinteger)

# # Following is the complex type of variable
# imaginary = 3 + 4j
# print(type(imaginary))


# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# address = "memory address of this string on memory"
# address1 = "memory address of this string on memory"

# this will print True because if the content is same then the same memory address will be allocated to the both of variables
# print(address1 is address)
# print(ord("a"))

# encoded_text = str.encode("asad")
# print(bytes.decode(encoded_text))

# empty_tuple = (1,)
# print(type(empty_tuple))


# byte code is not machine level language but it's easy for compiler to read because it's converted from highlevel langauge to bytecode
# See the below bytecode of multiply function using dis python built-in module
# import dis
# import example

# dis.dis(example)

# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# If you want to use set as dictionary key then we have to create the frozenset which is hashable means we can use it as a key in dictionary
# fset = frozenset([1, 2, 3, 4, 5])
# print(fset)

# if we use int and float both as a key in dict then two keys may pick the same value so avoid such situation and select unique keys in dict
# dictionary = {1: "one", 1.0: "floating one"}
# print(dictionary[1.0])

# nameRoll = {'asad':9123,'hamza':8975,'usman':9141}
# print(nameRoll)
# nameRoll['asad']

# cubes = [1, 8, 27, 65, 125]
# cubes[3] = 64
# cubes[2:4] = [3, 3]
# print(cubes)


# match case is like switch statement in other languages
# try:
#     status_code = int(
#         input(
#             """200 , 301 , 404 , 500 , 503
#         In the above given list enter status code to find information about it.
#         Enter anything beyond the above list will quit the program. """
#         )
#     )
# except ValueError:
#     print("You have enter the wrong value.")
# else:
#     match status_code:
#         case 200:
#             print(
#                 "This status code represent that request is successful and information is in the response."
#             )
#         case 201 | 202 | 203 | 204 | 205 | 206 | 207:
#             print("All Successful")
#         case 301:
#             print(
#                 "This website moved permanently to new location. Url is in the header."
#             )
#         case 404:
#             print("The server could not find the requested resource.")
#         case 500:
#             print("The error occurred on the server side.")
#         case 503:
#             print("Server is in maintenance state so keep visit after a while.")
#         case _:
#             print("You have enter the wrong input.")


# For loop alternative
# a = ["Mary", "had", "a", "little", "lamb"]
# for i in range(len(a)):
#     print(i, a[i])

# for index, value in enumerate(a, 1):
#     print(index, value)

# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# def passing(
#     *args,
# ):  # passing an arbitrary and infinite no of variable to this function.
#     a, b, c = args
#     print(args)
#     print(a)
#     print(b)
# passing(23, "asadpro", "BSCS")


# Rename the existing function with new name:
# from math import pow

# power = pow
# print(power(2, 4))


# positional argments (/) keyword arguments (*) dictionary **args
# def posKey(name, *, rollno):
#     print("Positional argument: ", name)
#     print("Keyword argument: ", rollno)


# posKey("asad", rollno=9124)

# args = [2, 11, 2]
# elements = list(range(*args))
# print(elements)

# Unpacking dictionary into in position arguments.
# def birds(name, color, voice):
#     print(f"Name of this bird: {name}")
#     print(f"Color of this bird: {color}")
#     print(f"Voice of this bird: {voice}")


# bird_dict = {"name": "Cow", "color": "Green", "voice": "Kagh Kagh"}

# birds(**bird_dict)

# 🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓
# numbers = [1, 8, 27, 65, 125, 27, 124]

# Appending to list in two ways
# numbers[len(numbers) :] = [145]
# numbers.append(155)

# Extending list in two ways
# second = [160, 170, 180]
# numbers.extend(second)
# numbers[len(numbers) :] = second

# Inserting element in list using two ways
# numbers[0] = 11
# But the following one will insert before element on 0 index
# numbers.insert(0, 11)

# Removing element from list in two ways.
# print("Before:", numbers)
# numbers.remove()

# Remove item from list using it's index
# print(numbers.pop(len(numbers) - 1))

# print("Number of occurrences: ", numbers.count(125))
# numbers.sort()
# newList = numbers.copy()
# print(id(newList))


# Find index of 27 start from index 4
# print(numbers.index(27, 4))
# print(numbers)

# 🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓
# Using lists as stack
# stack = [1, 2, 3, 4, 5, 6, 7, 8]

# # Removing element from stack
# for i in range(3):
#     stack.pop()

# # Adding element to stack
# start, stop = len(stack) + 1, len(stack) + 4
# for i in range(start, stop):
#     stack.append(i)
# print(stack)


# Using lists as queue
# queue = [1, 2, 3, 4, 5, 6, 7, 8]
# del queue[0]
# print(queue)

# Using deque class is efficient than using
# from collections import deque

# queue = deque([1, 2, 3, 4, 5, 6, 7, 8])
# print(list(queue))
# queue.popleft()
# print(queue)

# 🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓🥓
# Transpose rows and columns
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)
# comp_transpose = [[row[i] for row in matrix] for num in range(4)]
# print([[row[i] for row in matrix] for i in range(4)])
