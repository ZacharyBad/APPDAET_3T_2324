def is_armstrong(number: int, sigma: int) -> bool:
    # TODO: condition to check if the two parameters are equal
    return number == sigma

def get_sum(divisors: list[int]) -> int:
    # TODO: return the sum of all divisors
    return sum(divisors)

def get_cubed_divisors(potential_armstrong: int) -> list[int]:
    # TODO: return a list containing all digits cubed for this number
    # example:
    # get_cubed_divisors(153) should return [1, 125, 27]
    cubed_divisors = []
    for digit_char in str(potential_armstrong):
        digit = int (digit_char)
        cubed_divisors.append(digit ** 3)
    return cubed_divisors


def main():
    # 01: prompt user for a number and assign it to a variable named potential_armstrong
    potential_armstrong_str = input("Enter a number: ")
    
    # 02: condition to check if potential_armstrong (string) can be parsed to a number
    if potential_armstrong_str.isdigit():
        # 03: cast potential_armstrong to an integer
        potential_armstrong = int(potential_armstrong_str)
        
        # 04: call method get_cubed_divisors(potential_armstrong) and assign the returned value to a variable named cubed_divisors
        cubed_divisors = get_cubed_divisors(potential_armstrong)
        
        # 05: print the value of variable cubed_divisors
        print("Cubed divisors:", cubed_divisors)
        
        # 06: call method get_sum(divisors) and assign the returned value to a variable named sigma
        sigma = get_sum(cubed_divisors)
        
        # 07: print the value of variable sigma
        print("Sum of cubed divisors:", sigma)
        
        # 08: print the returned value of is_armstrong(potential_armstrong, sigma) method call
        print("Is Armstrong:", is_armstrong(potential_armstrong, sigma))
    else:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
