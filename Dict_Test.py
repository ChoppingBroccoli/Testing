prac_list = ['coin', 'dagger', 'sword']
prac_dict = {'coin': 23, 'dagger': 189, 'sword':1, 'ruby': 1}

print('Here are the contents of the Dictionary (aka inventory):')
print(prac_dict, '\n')


for every_dict_item in prac_dict:
    prac_dict.get(every_dict_item, 0)
    print('DEBUG FOR LOOP -- Dict item is ' + str(every_dict_item))
    for every_list_item in prac_list:
        if every_list_item != every_dict_item:
            print(str(every_list_item) + ' is in the List but not in your inventory')
        else:
            print('An item from the list (' + every_list_item + ') matches an item in your inventory (' + every_dict_item + ')')
            print('You have ' + str(prac_dict[every_dict_item]) + ' of these in inventory')
            

'''
Cannot print information about 'ruby'. For loop ends with sword. Likely because the list
does not have 'ruby' so it ends.

Need to find out why 'ruby' is not getting printed and add it to the Dict if it does not exist.

'''
