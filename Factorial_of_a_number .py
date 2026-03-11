num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# Print result
print(f"The factorial of {num} is {factorial}")

OUTPUT:
Enter a number: 7
The factorial of 7 is 5040
