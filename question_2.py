#Task 1:

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))

if num1 >= num2 and num1 >= num3:
    print(str(num1) + " is the largest")
elif num2 >= num1 and num2 >= num3:
    print(str(num2) + " is the largest")
else:
    print(str(num3) + " is the largest")

#Task 2:

if num1 < num2 and num1 < num3:
    print(str(num1) + " is the smallest")
elif num2 < num1 and num2 < num3:
    print(str(num2) + " is the smallest")
else:
    print(str(num3) + " is the smallest")

#Task 3:

if num1 == num2 and num1 == num3:
    print("They are all " + str(num1))
elif num2 == num1 and num2 > num3:
    print(str(num2) + " is the same as the first and they are the largest")
elif num3 == num1 and num2 > num1:
    print(str(num3) + " is the same as the first but the second number is the largest")
elif num2 == num3 and num2 > num1:
    print(str(num3) + " is the same as the second number and they are the largest")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("There are two numbers that are the same")
else:
    print(str(num3) + " is the largest")
