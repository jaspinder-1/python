class Rectangle():
  def __init__(self, length, width):
    self.length = length
    self.width = width
  
  def rect_area(self):
    return self.length * self.width

if __name__ == "__main__":
  obj = Rectangle(5, 6)
  area = obj.rect_area()
  print area
