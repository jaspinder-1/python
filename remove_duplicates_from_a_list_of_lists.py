list_of_list = [[1,1,2],[2,4],['a','a','b']]
new_list = [list(set(x)) for x in list_of_list]
print new_list
