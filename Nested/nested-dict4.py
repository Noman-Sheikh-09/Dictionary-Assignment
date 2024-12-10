#25.	Delete the Address key from the nested dictionary.


person={
    "name" : "Hafiz Muhammad Rehan" ,
    "age": 19,
    "address":{
        "street": "P-485 D block millat town",
        "city": "Faisalabad"
    }
}

for key in person.keys():
    print("The key is: ",key)

user_input=input("Enter the key which you want to delete: ")

if user_input in person:

    if user_input == "address":
        #user_input_for_yes_no=input("Enter Yes or no: ").lower()
        # if user_input_for_yes_no == "yes":
        for key in person["address"].keys():
                    print(f"The address key :{key}")

        user_input_for_key=input("Enter the key which you want to delete: ").lower()
        del person["address"][user_input_for_key]
        print(f"\t\t\tThe Dictionary without {user_input_for_key}")
        #print(f"The dictionary is {person}")
        for key,value in person.items():
            print(key,":",value)

        #else:
        #   print("No problem")
    else:

        print(f"\t\t\t\tThe dictionary without {user_input}")
        del person[user_input]
        for key,value in person.items():
                print(key,":",value)
        #print(person)

else:
    print(f"\t\t\t\tYou enter {user_input} is not key in dictionary..")        
