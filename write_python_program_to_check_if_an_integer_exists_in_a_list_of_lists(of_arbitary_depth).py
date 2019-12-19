our_list = ['a','b',['a',['a','a',['h',['1',[1]]]]]]

def int_exists(our_list):
    for x in our_list:
      if type(x) == int:
        return "Integer exists"
      elif type(x) == list:
        return int_exists(x)
    else:
      return 'Integer not found'
      

if __name__ == "__main__":
  x = int_exists(our_list)
  print x
