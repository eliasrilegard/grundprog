n = int(input("Enter a value: "))           # Ask user for value (should be an integer)
limit = int(n**(1./3)) + 1                  # The highest number (limit) cannot be higher than the cubic root of n
                                            # Adding 1 because the range() starts from 0 (zero)
list_solution = []                          # Defining list to store solutions

for a in range(1, limit):                   # Since 3rd square root of 1729 does not provide a whole number, start from 1
    for b in range(a, limit):               # Iterating through each a and b, so that first a = 1 iterates through every b (up to limit), then a = 2, and so on
        if a**3 + b**3 == n:                # A match is found if the cubic values of the integers is equals to n
            list_solution.append((a, b))    # That solution is added to the solution list
print(list_solution)                        # When all iterations are concluded, the answers are printed
                                            # If no answers are found, then it will print [].
