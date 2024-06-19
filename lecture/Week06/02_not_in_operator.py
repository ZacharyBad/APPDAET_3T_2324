fruits = [
    "apple",
    "pomegranate",
    "kiwi",
    "salak",
    "blackberry"
]


fruits_to_find = "kiwi"

for fruit  in fruits:
    if fruits_to_find == fruit:
        print(f"{fruit} is  EQUAL")
    else:
        print (f"{fruit} is  {fruits_to_find}")


print(f"is {fruits_to_find} not in {fruits}? {fruits_to_find not in fruits}")
print (f"{fruits_to_find not in fruits}")

print("----SUPERSTARS----")
superstars = [77, 15, 2, 34, 0]
print(23 not in superstars)
print(35 not in superstars)
print(77 not in superstars)