#Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
def accept_key(dictionary,key):
    return dictionary.get(key,"\n\t\t\t\tKEy not find")
dictionary_user={'name': 'Rehan', 'age': 19, 'grade': 'A',"roll number":245289,"semester":"First Evening-B","phone":+923019201234,"university":"Government University of Faislabad"}
while True:
    
    
    user_input=input("Enter the key which you want and q for quit : ").lower()
    if user_input == "q":
        quit()
    else:    
        func=accept_key(dictionary_user,user_input)
        print(func)
        