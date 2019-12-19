names = ['car','car','car']

def all_exists(our_list, word):
  return all(word==x for x in our_list)

if __name__ == "__main__":
  print all_exists(names, 'car')
