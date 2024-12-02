def is_perfect(number: int, sigma: int) -> bool:
      #todo condition to check if the two parameters are equal
      if number == sigma:
            return True
      else:
            return False
      
      # or we can do
      #return number == sigma
      return

def get_sum(divisors: list[int]) -> int:
      # TODO: return the sum of all divisors

      #option 1 : loop through each item on the list
      #sigma = 0
      #for i in divisors:
      #   print(f"divisor is {i}")
      #      sigma += i
      #return sigma
      #option 2  use the sum function
      return sum(divisors)

def get_divisors(midterm_number: int) -> list[int]:
     #TODO: return a list containing all divisors for this number
     #1 should always be included
     divisors = []
     for i in range(1, midterm_number):
           if midterm_number % i == 0:
                 divisors.append(i)
     return divisors

def main():
     # 01 prompt a user a number and assign it to a variable (miderm_number)
     midterm_number = input ("Please enter a number: ")
     # 02: condition to check if midterm_number (string) can be parsed to a number
     if not midterm_number.isnumeric(): #replaced the if else and added a not before the variable to make it cleaner
            print("This is not a number")
     # 03: cast midterm_number to an integer
     else:
            midterm_number = int(midterm_number) #added an else with the if to make it shorter and make it more clean
     # midterm_number = int(midterm_number) this is how you cast/convert the str(check by hovering midterm_number) into an int.

     # 04: call method get_divisors(midterm_number) and assign the returned value to a variable named divisors
     divisors = get_divisors(midterm_number)
     #05: print the value of variable divisors
     print(f"divisors: {divisors}")
     #06: call method get_sum(divisors) and assign the returned value to a variable named sigma
     sigma = get_sum(divisors)
     #07: print the value of  variable sigma
     print(f"sigma is {sigma}")
     #08: print the returned value of is_perfect(midterm_number , sigma) method call
     print(f"is perfect is {is_perfect(midterm_number, sigma)}")
if __name__ == "__main__":
        main()