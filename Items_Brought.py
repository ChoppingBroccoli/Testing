allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples      ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups      ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes      ' + str(totalBrought(allGuests, 'Cakes')))
print(' - Ham Sandwiches      ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apples Pies      ' + str(totalBrought(allGuests, 'apples pies')))

'''
Things to test with:
1) Create a "board" to print all the items in. This will make everything line up
and look nice.
2) Print the values dynamically. Instead of print(' - Apples  ') why not
do it dynamically so 'Apples' can become something else in the future?
'''
