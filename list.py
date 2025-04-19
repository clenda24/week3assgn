# create an empty list
my_list = []

# append 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert (15) at the second position 
my_list.insert(15)

# extend my_list with another list
my_list.extend([50, 60, 70])

# remove the last element
my_list.pop()

# sort my_list in ascending order
my_list.sort()

# find and print the index of the value of 30 in my my_list
index_of_30 = my_list.index(30)
print(index_of_30)
