#23.	Access the value of the City key in the nested dictionary from the previous question.


person={
    "name" : "Hafiz Muhammad Rehan" ,
    "age": 19,
    "address":{
        "street": "P-485 D block millat town",
        "city": "Faisalabad"
    }

}
for key in person.keys():
    print(f"\t\t\tThe keys are:{key}")

user_input=input("Enter the key: ")
if user_input in person:
    if user_input == "address":
        user_input_for_address=input("Enter the city or street:")
        address_dict=person["address"][user_input_for_address]
        print(address_dict)

    elif user_input != "address":
        calling_city=person[user_input]
        print(calling_city)
   

else:
    print("Invalid")