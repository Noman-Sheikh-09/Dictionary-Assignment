#Remove the key city from the student dictionary.
student_info={
            "name":"Rehan",
            "age":19,
            "grade":"A"
            
            }

print(f"\tThe Dictionary is:\n\t\t{student_info}")
user_input_remove_key=input("\tEnter the key which you want to remove it")
print(f"\n\t\t\t5.After removing ")
del student_info[user_input_remove_key]

print(f"The dictionary after remove the {user_input_remove_key}:\n\t\t\t{student_info}")
