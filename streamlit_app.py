def find_greatest_number(a, b, c):
    if a > 2 and b > 2 and c > 2:
        return max(a, b, c)
    else:
        return "All three numbers must be greater than 2."

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding and printing the greatest number
result = find_greatest_number(num1, num2, num3)
print(result)
