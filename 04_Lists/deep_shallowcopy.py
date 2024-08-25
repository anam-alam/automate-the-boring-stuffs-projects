import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#new_list = copy.copy(old_list)
new_list = copy.deepcopy(old_list)

#old_list.append([4, 4, 4])
old_list[2][2] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)

print("Old list:", id(old_list))
print("New list:", id(new_list))


'''
  Output for shallow copy when just appending the old_list

    Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [4, 4, 4]]
    New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Old list: 2391956330944
    New list: 2391956330816
'''

'''
    Output for shallow copy when changing the list[1] inside the old_list

    Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 'BB']]
    New list: [[1, 2, 3], [4, 5, 6], [7, 8, 'BB']]
    Old list: 2639157866752
    New list: 2639157867136

    both lists value are change because both lists share the reference of same nested objects.
'''


'''
    Output for deep copy when changing the list[1] inside the old_list

    Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 'BB']]
    New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Old list: 1991940649216
    New list: 1991940649600
'''

'''for deepcopy
    when we assign a new value to old_list, we can see only the old_list is modified. 
    This means, both the old_list and the new_list are independent.
    This is because the old_list was recursively copied, which is true for all its nested objects.
'''