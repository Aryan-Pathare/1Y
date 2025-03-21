# Python program to check if a number is prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get input from user
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")