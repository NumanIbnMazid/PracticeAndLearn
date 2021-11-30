# Question:

# Prime Time
# Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is a prime number, otherwise return the string false. The range will be between 1 and 2^16.
# Examples
# Input: 19
# Output: true
# Input: 110
# Output: false


# Submission:

def PrimeTime(num):
  is_prime = False
  # code goes here
  # if num <= 1:
  #   return False
  for n in range(1, 2^16):
    if num > 1:
      if not n == num:
        if num % n == 0:
          is_prime == False
      else:
        if num % num == 0:
          is_prime = True
    else:
      is_prime = False
  return str(is_prime).lower()

# keep this function call here 
print PrimeTime(raw_input())
