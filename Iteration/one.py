#6.	Iterate through the dictionary student and print all keys.

student_info={
            "name":"Rehan",
            "age":19,
            "grade":"A"
            
            }


print("\n\t\t\t\t6.print all keys")

for keys,values in student_info.items():
    print(f"The key are:{keys}")
    print(f"\tThe values are:{values}")            