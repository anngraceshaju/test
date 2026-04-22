class Maths:
    def area(self):
        pass

class Circle(Maths):
    def __init__(self,radius):
     self.radius=radius
     print("area" ,3.14*radius*radius)


c=Circle(20)

class Rect(Maths):
   def __init__(self,length,breadth):
      self.length=length
      self.breadth=breadth
      print("area is",length*breadth)

d=Rect(3,4)

class Square(Maths):
   def __init__(self,a):
      self.a=a
      print("area is",a)

b=Square(5) 
    