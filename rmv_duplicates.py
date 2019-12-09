samp_list = [1,2,3,2,1,4,5,6]
new_list = []
for x in samp_list:
  if x not in new_list:
    new_list.append(x)
print new_list
