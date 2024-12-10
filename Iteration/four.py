#9.	Check if the key grade exists in the student dictionary and print True or False


student_info={
            "name":"Rehan",
            "age":19,
            "grade":"A"
}
            #print(f"The Dictionary is:\n\t\t{student_info}")
        
print(f"\t9.Check if the key grade exists in the student dictionary ")

        #for keys,values in student_info.items():
if  "grade" in student_info:
                    print(f"\t\t\t\tGrade is available..")
                   
                    
else:
                    print(f"\t\t\t\tGrade is not available..")   