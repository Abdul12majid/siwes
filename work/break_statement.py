# break
def find_prime_numbers(upper_bound):
  """Finds all prime numbers up to a given upper bound.

  Args:
    upper_bound: The upper bound for the prime number search.

  Returns:
    A list of all prime numbers up to the given upper bound.
  """

  primes = []
  for i in range(2, upper_bound + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
      if i % j == 0:
        is_prime = False
        break

    if is_prime:
      primes.append(i)

  return primes


def main():
  """Prints all prime numbers up to 100."""

  primes = find_prime_numbers(100)

  for prime in primes:
    print(prime)

  # Break out of the loop if the user enters "q"
  while True:
    user_input = input("Enter another upper bound (or q to quit): ")
    if user_input == "q":
      break

    try:
      upper_bound = int(user_input)
    except ValueError:
      print("Invalid input.")
      continue

    primes = find_prime_numbers(upper_bound)

    for prime in primes:
      print(prime)


if __name__ == "__main__":
  main()


def binary_search(array, target):
  """Performs a binary search for the given target in the given array.

  Args:
    array: A sorted array of elements.
    target: The element to search for.

  Returns:
    The index of the target element in the array, or -1 if the target element
    is not found.
  """

  low = 0
  high = len(array) - 1

  while low <= high:
    mid = (low + high) // 2

    if array[mid] == target:
      return mid
    elif array[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  # Break out of the loop if the target element is not found.
  return -1


def main():
  """Searches for a given element in a sorted array using binary search."""

  array = [1, 3, 5, 7, 9]

  target = int(input("Enter the element to search for: "))

  index = binary_search(array, target)

  if index != -1:
    print(f"The element {target} is found at index {index}.")
  else:
    print(f"The element {target} is not found in the array.")


if __name__ == "__main__":
  main()
