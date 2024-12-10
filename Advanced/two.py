#14.	Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.

unsort_dict={'z': 1, 'a': 2, 'c': 3}
       # print(f"\t\tThe unsorting Dictionary: \t{unsort_dict}")

sort_dict=dict (sorted(unsort_dict.items() )  )
print(f"\n\tUnsorted Dictionary: {unsort_dict}")

print(f"\n\t\t\tSorted dictionary{sort_dict}")

