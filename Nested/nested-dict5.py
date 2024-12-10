#26.	Iterate through all the keys in the outermost level of the nested dictionary and print them.

person={
    "name" : "Hafiz Muhammad Rehan" ,
    "age": 19,
    "address":{
        "street": "P-485 D block millat town",
        "city": "Faisalabad"
    }
}


for key in person.keys():
    if key == "address":
        for address_key in person["address"].keys():
            print(f"The keys of address are ({address_key})")

