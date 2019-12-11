temp = []
def highest_sum(list):
  for i,x in enumerate(list):
    temp.append(sum(x))
  index = highest_list(temp)
  return list[index]

def highest_list(sum_list):
  index = sum_list.index(max(sum_list))
  return index

print highest_sum([[1,2,3],[1],[2,7],[1,1],[11,4]])
