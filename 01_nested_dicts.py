atrium = {
    "name": "The Atrium @ benilde",
    "Floors": {
        "G":{
            "amenities": [
                "entrance",
                "exit",
                "Vatel Restaurant"
            ],
            "lavatories": "1"
        },
        "M": {},
        "2": {},
        "3": {
            "Amenities": [
                "Clinic"
            ],
            "lavatories": "1"
        }
    }
}

print (f"Amenities of the G Floor: {atrium['floors']['G']['amenities']}")

# atrium ["floors"].items()
#   -returns a tuple
#       - 1st element is the key
#       - 2nd element is the value
for floor in atrium["floors"].items():
    print(floor)

#atrium["floors"]
#   - if atrium["floors"] is a dictionary
#       - returns a string which is the key
for floor in atrium["floors"]:
        print(floor)
#atrium["floors"].keys();
#   - if atrium["floors"] is a dictionary
#       - returns a string which is the key
#           - same with actual floors
for floor in atrium["floors"].keys():
        print(floor)

#atrium["floors"].values()
#   -if atrium["floors"] is a dictionary
#       - returns the value for each item
for floor in atrium["floors"].values():
        print(floor)


