#29.	Write a Python program to split a dictionary into two based on whether the values are odd or even

dictionary_num={"a":2,"b":3,"c":4,"d":6,"e":5,"f":7}
new_dict={"g":8,"h":9,"i":10}

dictionary_num.update(new_dict)

reverse=dictionary_num.__reversed__()


even_num={f"{k}:{v}" for k,v in dictionary_num.items() if v%2==0}
odd_num={f"{k}:{v}" for k,v in dictionary_num.items() if v%2!=0}


print("Even-numbers=",even_num)
print("Odd-numbers= ",odd_num)
