"""
- Lists are an aggregate data type, meaning that they are composed of other data types

 - Similar to strings, the values inside them are indexed and have a
 length property to count the number of items inside of them

 - Python lists can hold values of different types()

 - Python lists are mutable 
"""

lotto_numbers = [19, 10, 88, 4, 22, 91]
print (lotto_numbers)

course = ["A", "P", "P", "D", "A", "E", "T"]
print(course)
print("".join(course))

mixed_list = [1, 3.1419, "Spring", "Summer", [1, 2, 3, 4]]
print(mixed_list)

print(len(mixed_list))