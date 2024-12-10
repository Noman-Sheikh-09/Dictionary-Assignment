#8.	Iterate through the dictionary student and print all key-value pairs in the format key: value.



student_info={
            "name":"Rehan",
            "age":19,
            "grade":"A"
            
            }


print("\n\t\t\t\t8.print all keys in key: value\n")

for keys,values in student_info.items():
            print("\t\t\t",keys,":",values)