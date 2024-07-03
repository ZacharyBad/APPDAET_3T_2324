def is_armstrong(number: int) -> bool:
    # Convert the number to a string to easily iterate over digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == number

def get_sum(divisors: list[int]) -> int:
    return sum(divisors)

def get_divisors(midterm_number: int) -> list[int]:
    divisors = [] 
    for i in range(1, midterm_number):
        if midterm_number % i == 0:
            divisors.append(i)
    return divisors

def main():
    midterm_number = input("Please enter a number: ")
    if not midterm_number.isnumeric():
        print("this is not a number")
    else:                  
        midterm_number = int(midterm_number)
        divisors = get_divisors(midterm_number)        
        print(f"divisors: {divisors}")

        sigma = get_sum(divisors)
        print(f"sigma is: {sigma}")
                
        print(f"is_armstrong is {is_armstrong(midterm_number)}")

if __name__ == "__main__":
    main()
