"""
The input method will take a raw input from user 
whereas eval method will evaluate the expression given into it 
as python statement
"""
# name = input("Enter your name : ")
# print("Your name is : {}".format(name))

# result = eval(input("Enter any expression to evaluate : "))
# print("The number you have multiplied are: {}".format(result))


# 🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱

# names = input("Enter name separated by commas : ").split(",")
# assignments = input("Enter assignments counts separated by commas : ").split(",")
# grades = input("Enter grades separated by commas : ").split(",")


# for name, assignment, grade in zip(names, assignments, grades):

#     message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
#     submit before you can graduate. You're current grade is {} and can increase \
#     to {} if you submit all assignments before the due date.\n\n".format(
#         name, assignment, grade, int(grade) + int(assignment) * 2
#     )
#     print(message)


# 🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱


# def party_planner(cookies, people):
#     leftovers = None
#     num_each = None
#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except ZeroDivisionError:
#         print("You input a different number of people")

#     return (num_each, leftovers)


# # The main code block is below; do not edit this
# lets_party = "y"
# while lets_party == "y":

#     cookies = int(input("How many cookies are you baking? "))
#     people = int(input("How many people are attending? "))

#     cookies_each, leftovers = party_planner(cookies, people)

#     if cookies_each:  # if cookies_each is not None
#         message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
#         print(message.format(people, cookies_each, leftovers))

#     lets_party = input("\nWould you like to party more? (y or n) ")

# 🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱

# with open("C:\\Users\\User\\Desktop\\Python_Nano_Degree\\file.txt", "r") as file:
#     for line in file.readlines():
#         print(line.strip("\n"))


# with open("C:\\Users\\User\\Desktop\\Python_Nano_Degree\\file.txt", "r") as file:
#     for line in file.readlines():
#         print(line.strip("\n"))

# names = []
# with open("flying_circus_cast.txt", "r") as file:
#     content = list(file)
#     for element in content:
#         newlist = element.split(", ")
#         names.append(newlist[0])
# for name in names:
#     print(name)

# Alternative solution to the above problem
# cast_list = []
# with open("flying_circus_cast.txt") as f:
#     for line in f:
#         name = line.split(",")[0]
#         cast_list.append(name)


# 🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱
# import math
# from math import exp

# print(exp(3))

# import random

# word_list = [
#     "script",
#     "buggy",
#     "random",
#     "choice",
#     "bekin",
#     "passphrase",
#     "mount",
#     "william",
#     "turner",
# ]
# password = ""
# def generate_password():
#     return "".join(random.sample(word_list, k=3))
# print(generate_password())

# Another alternative to the aforementioned solution
# import random

# word_file = "words.txt"
# word_list = []

# with open("words.txt") as readfile:
#     for line in readfile:
#         word = line.strip().lower()
#         if 3 < len(word) < 8:
#             word_list.append(word)


# def generate_password():
#     return "".join(random.sample(word_list, k=3))


# print(generate_password())

# 🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱
# Extracting zip file using python module zipfile
# from zipfile import ZipFile

# with ZipFile("sample.zip") as zip:
# zip.printdir()            # printdir method will print all the meta data of the file to the prompt
# print(zip.namelist())     # namelist method will list out all the file contain in archive
# zip.extract("words.txt")


# with ZipFile("sample.zip") as zip:
#     # Extracting information of zip file using ZipFile class from the zipfile module
#     strin = str(zip.infolist()[0])
#     rawlist = strin.split()
#     rawlist.pop(0)
#     new_word = []
#     for word in rawlist:
#         temp = word.split("=")
#         new_word.extend(temp)

#     name_value = {}
#     safe_list = []
#     count = 0
#     for key in new_word:
#         safe_list.append(key.strip(">").strip("'"))

#     # for key in safe_list:
#     for index in range(len(safe_list)):
#         if index == 0:
#             name_value[safe_list[index]] = safe_list[index + 1]
#         elif index == len(safe_list) - 1:
#             name_value[safe_list[index]] = safe_list[index]
#             break
#         elif index % 2 == 1:
#             name_value[safe_list[index]] = safe_list[index + 1]
#     for key, value in name_value.items():
#         print(key, value)

# 🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱

# my_list = ["element1\t0238.94", "element2\t2.3904", "element3\t0139847"]

# element_list = []
# clear_list = []
# for value in my_list:
#     element_list.extend(value.split("\t"))

# for index in range(len(element_list)):
#     if index == 0:
#         clear_list.append(element_list[index])

#     elif index % 2 == 1:
#         continue
#     else:
#         clear_list.append(element_list[index])
# print(clear_list)


# The alternative solution to the above problem
# clear_list = [i.split("\t", 1)[0] for i in my_list]
# print(clear_list)


# Same solution using lambda and map method

# lambda_list = list(map(lambda element: element.split("\t")[0], my_list))
# print(lambda_list)

# 🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱🍱

import string
import os

# print(string.digits)
# print(string.ascii_letters)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)

print(os.path)
