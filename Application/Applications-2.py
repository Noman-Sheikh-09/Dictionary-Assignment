#22.	Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
#dictionary={"a":10,"b":12,"c":14,"d":16}

#a built-in function that allows you to access the value of an item associated with the specified key.
#print(f"The dictionary is {dictionary}")
#max_num=max(dictionary,key=dictionary.get)

#print(f"\n\t\t\tThe  value of {max_num} is maximum in your dictionary  ")



user_dict={}

n=int(input("Enter a number how many items do you want to add: "))

for i in range(n):
    key=input(f"Enter key {i+1}: " )
    value=input(f"Enter value for key {key}: ")
    user_dict[key]=value

print(user_dict)

if user_dict:
    max_key_user=max(user_dict,key=user_dict.get)
    print(f"The key with the maximum value in your dictionary is {max_key_user} with the value of {user_dict[max_key_user]}")

else:
    print("The dictionary is empty ")        


