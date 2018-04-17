prac_list = ['coin', 'dagger', 'sword']
prac_dict = {'coin': 3, 'dagger': 2, 'sword':1, 'ruby': 1}

for every_dict_item in prac_dict:
    prac_dict.get(every_dict_item, 0)
    for every_list_item in prac_list:
        if every_list_item == every_dict_item:
            print ('The item from the list matches an item from the dictionary')
            print('List item was ', every_list_item)
            print('Dict item was ', every_dict_item)


'''
Prints items from both the list and dict objects and does some checking. I want it to print the Dict and the List
Want to adjust the print statements to better understand/see what the program is
 doing at each iteration.

Want to print each key-value pair before and after running through loops

'''
