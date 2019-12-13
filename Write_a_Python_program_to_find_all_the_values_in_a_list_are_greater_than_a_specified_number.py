num = int(raw_input('Enter a number: '))
our_list = [11,10,6]

def all_greater_than(our_list):
  for i in our_list:
      if i > num:
          return True
  return False
