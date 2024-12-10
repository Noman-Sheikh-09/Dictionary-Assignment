#Flatten the following nested dictionary into a single-level dictionary:

nested_list={"a":{
    "b":1,
    "c":2,
    "d":3
},


}
print("Ourself logic of chatgpt ")
for key,sub_dict in nested_list.items():
    for sub_key,sub_value in sub_dict.items():
        print({f"{key}-{sub_key}:{sub_value}"})



print("With the help of chat-gpt  ")
flatten_dict={f"{key}-{sub_key}":sub_value for key,sub_dict in nested_list.items() for sub_key,sub_value in sub_dict.items() }

print(flatten_dict)
