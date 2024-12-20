numbers = (1, 2, 3, 4, 5)

sum_numbers = sum(numbers)
print(f"Sum of all numbers: {sum_numbers}")

largest_number = max(numbers)
print(f"Largest number: {largest_number}")

smallest_number = min(numbers)
print(f"Smallest number: {smallest_number}")

import random
random_numbers = tuple(random.randint(1, 10) for _ in range(5))
print(f"Random numbers: {random_numbers}")

number_to_check = 7
if number_to_check in random_numbers:
    print(f"{number_to_check} exists in the tuple.")
else:
    print(f"{number_to_check} does not exist in the tuple.")
