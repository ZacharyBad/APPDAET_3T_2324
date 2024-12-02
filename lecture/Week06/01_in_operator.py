fruits = [
    "apple",
    "pomegranate",
    "kiwi",
    "salak",
    "blackberry"
]

#problem:
# How would you check if "Kiwi" is in fruits?

# 1. Via for loop
fruits_to_find = "kiwi"

for fruit in fruits:
    if fruits_to_find == fruit:
        print(f"{fruit} is EQUAL")
    else:
        print (f"{fruit} is not {fruits_to_find}")

#2 "in" operator
print(f"is {fruits_to_find} in {fruits}? {fruits_to_find in fruits}")
print (f"{fruits_to_find in fruits}")

print("----SUPERSTARS----")
superstars = [77, 15, 2, 34, 0]
print(23 in superstars)
print(35 in superstars)
print(77 in superstars)