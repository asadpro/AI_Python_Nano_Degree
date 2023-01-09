"""
Zip are used to store tuple of information in a single list like if we want to store information of alphabet with their respective unicode number 
then we can do the follow.
Now you may also ask why not to use dictionary well in that case dictionary isn't very efficient like zip function you will see it latter.
"""
# letters = ["a", "b", "c"]
# nums = [1, 2, 3]

# for letter, num in zip(letters, nums):
#     print("{}: {}".format(letter, num))


"""
We can also unzip multiple iterators wrap up in a single list like below
"""
# unziped = [("hamza", 3.4), ("saeed", 2.8), ("saqib", 3.6)]
# name, gpa = zip(*unziped)
# print(name)
# print(gpa)

# 🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿
"""
Enumerate will return an iterator that contain value and it's index.
"""

# alphabet = ["a", "b", "c", "d", "e"]
# for index, value in enumerate(alphabet):
#     print("{} : {}".format(index, value))


"""
The length of the resulting tuples will always be equal to the number of iterable you have passed."""
# integers = [1, 2, 3]
# letters = ["a", "b", "c"]
# floats = [4.0, 5.0, 6.0]
# for integ, lett, flt in zip(integers, letters, floats):
#     print(f"{0} : {1} : {2} :", integ, lett, flt)


# 🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗

"""
Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends 
it to the list points. Each string should be formatted as label: x, y, z. For example, 
the string for the first coordinate should be F: 23, 677, 4.
"""
# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

# points = []

# # write your for loop here

# for point in zip(labels, x_coord, y_coord, z_coord):
#     print(
#         "{}: {}, {}, {}".format(*point)
#     )  # The asterik will unzip the tuple which contain 4 elements
#     points.append(point)

# 🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗

# Use zip to create a dictionary cast that uses names as keys and heights as values.

# cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
# cast_heights = [72, 68, 72, 66, 76]

# cast = dict(zip(cast_heights, cast_names))
# print(cast)


# Transpose the tuple from 4-by-3 matrix to 3-by-4 matrix.
# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

# data_transpose = list(zip(*data))
# print(data_transpose)

# 🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗

"""
Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. 
For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".
"""
# cast = [
#     "Barney Stinson",
#     "Robin Scherbatsky",
#     "Ted Mosby",
#     "Lily Aldrin",
#     "Marshall Eriksen",
# ]
# heights = [72, 68, 72, 66, 76]

# for i, cst in enumerate(cast):
#     cast[i] = f"{cst} {heights[i]}"

# print(cast)

# 🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# first_names = [name.split()[0].lower() for name in names]
# print(first_names)


# Create a list that contain only those names which have score more than 65
# scores = {
#     "Rick Sanchez": 70,
#     "Morty Smith": 35,
#     "Summer Smith": 82,
#     "Jerry Smith": 23,
#     "Beth Smith": 98,
# }

# passed = [key for key, value in scores.items() if value >= 65]
# print(passed)


# 🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗


"""
Write a function named population_density that takes two arguments, population and land_area, 
and returns a population density calculated from those values.
I've included two test cases that you can use to verify that your function works correctly. 
"""
# write your function here


# def readable_timedelta(days):

#     weeks = 0
#     day = 0
#     while days != 0:
#         if days >= 7:
#             weeks += 1
#             days = days - 7
#         else:
#             day = days
#             break
#     return "{} week(s) and {} day(s).".format(weeks, day)


# print(readable_timedelta(39))


# The alternative to the above solution is below.

# def readable_timedelta(days):
#     weeks = days // 7
#     day = days % 7
#     return "{} week(s) and {} day(s).".format(weeks, day)


# print(readable_timedelta(7))

# 🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗
"""
lambda expression is very vital for small amount of calculation but it isn't ideal selection for complex problem
"""

# double = lambda num: 23 * 5
# print(double(4))


# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x**2, numbers)
# print(list(squared_numbers))


cities = [
    "New York City",
    "Los Angeles",
    "Chicago",
    "Mountain View",
    "Denver",
    "Boston",
]


# def is_short(name):
#     return len(name) < 10

"""
Below filter method return which we have to convert it to list or any other data structure so that we can see it.
Now below 'city' is the argument of function (lambda expression) and in the body section we have to define the operation 
we want to perform on it and at last is the iterable which gives us elements one by one so that we perform action on it.
"""

# short_cities = list(filter(lambda city: len(city) < 10, cities))
# print(short_cities)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

filter_method = list(filter(lambda x: x % 2 == 0, numbers))

map_method = list(map(lambda x: x % 2 == 0, numbers))

reduce_method = reduce(lambda x, y: x + y, numbers)

print(filter_method)
print(map_method)
print(reduce_method)
