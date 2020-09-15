def ramanujan(n):                               # Defining a function that takes n as an argument
    limit = int(n**(1./3)) + 1                  # Same code as in uppgift4.py
    set_solution = set()                        # Check for any comments there
    for a in range(1, limit):
        for b in range(a, limit):
            if a**3 + b**3 == n:
                if b > a:                       # Here we check so that no copies are added
                    set_solution.add((a, b))
                else:
                    set_solution.add((b, a))
    return list(set_solution)                   # Return set_solution as a list

n = int(input("Enter a value: "))               # Asking user for a value
print(ramanujan(n))                             # Calling the function and giving it the argument n
