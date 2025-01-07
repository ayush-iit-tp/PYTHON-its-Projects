def is_prime(num):
    if num <= 1:
        return False
    if num == 2: return True  # 2 is the only even prime number
    if num % 2 == 0: return False # Exclude other even numbers
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0: return False
    return True

# Example usage
number = int(input("Enter a number: "))
print(int(number**0.5))
print(int(number**0.5) + 1)
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
