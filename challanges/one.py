#27.	Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.

user_input=int(input("Enter the number: "))

cude_root={num:num**3 for num in range(1,user_input+1)}

print(cude_root)