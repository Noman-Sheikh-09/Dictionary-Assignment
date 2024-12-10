#11.	Merge the following two dictionaries and print the result:
#12.	dict1 = {'a': 1, 'b': 2}  
#dict2 = {'c': 3, 'd': 4}  


dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4}  

dict1.update(dict2)
print(f"After merging dictionary: {dict1}")