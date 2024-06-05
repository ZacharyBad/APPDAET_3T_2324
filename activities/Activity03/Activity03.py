import sys

def print_name_card(first_name, last_name):
    border = "_" * 20
    print(border)
    print("| First Name:" + first_name)
    print("| Last Name:" + last_name)
    print(border)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python activity03.py <FirstName> <LastName>")
        sys.exit(1)
    
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    print_name_card(first_name, last_name)
