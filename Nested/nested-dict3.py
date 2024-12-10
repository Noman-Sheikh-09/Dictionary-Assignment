#24.	Add a new key Phone to the nested dictionary with the value "123-456-7890".

person={
    "name" : "Hafiz Muhammad Rehan" ,
    "age": 19,
    "address":{
        "street": "P-485 D block millat town",
        "city": "Faisalabad"
    }
}
user_input_for_permission=input("Do you want to add a number.Enter Yes/no:").lower()
if user_input_for_permission == "yes":
    add_number=int(input("Enter a number in 123-456-7890 format: "))


    person["Phone-number"]=add_number
    print(person)
else:
    print("\t\t\t\tYou do not add a key")
    print(f"\t\t\tYour dictionary without addition a key {person}")

#print(f"Dictionry without add a key..{person}") 



