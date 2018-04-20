prac_list = ['coin', 'dagger', 'sword']
prac_dict = {'coin': 23, 'dagger': 189, 'sword':1, 'ruby': 1}

print('Here are the contents of the Dictionary (aka inventory):')
print(prac_dict, '\n')

list_it = 0
for dict_item in prac_dict:
    prac_dict.setdefault(dict_item, 0)
    print('--DEBUG--')
    print('Dictionary item is ' + str(dict_item))
    print('We are comparing ' + str.upper(prac_list[list_it]) + ' from the List with ' + str.upper(dict_item) +
          ' from the Dictionary')
    list_it += 1
    for list_item in (range(len(prac_list) + 1)):
        if prac_list[list_item] != dict_item:
            print(str.upper(prac_list[list_item]) + ',from the List, is not in your inventory')
        else:
            print(str.upper(prac_list[list_item]) + ', from the List matches ' + str.upper(dict_item) + ' in the Dictionary')
            print('You have ' + str(prac_dict[dict_item]) + ' of these in inventory' + '\n')
            break

'''
Cannot print information about 'ruby'. For loop ends with sword. Likely because the list
does not have 'ruby' so it ends.

Need to find out why 'ruby' is not getting printed and add it to the Dict if it does not exist.

'''
