#numberone

def isScalene(x, y, z):
  if x == y == z:
    print("Equilateral")
  if x != y != z:
    print ("Scalene")
    return True
  else:
    print("Isosceles")

isScalene(12, 6, 2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#numbertwo

list = []

inputv = input("Print a number up to 100 to generate a list (e.g. 1 to _):")

def generatenumbers(start, end):
  for i in (range(1, end)):
    list.append(i)

generatenumbers(1, int(inputv))
print(list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#numberthree(a)


a = input("Choose one number:")
b = input("Choose another number:")

def getBiggerNumber(x,y):
  if a < b:
    print(b, "is the greater number")
  if a > b:
    print(a, "is the greater number")
  if a == b:
    print(a, "is equal to", b,";" " " "Therefore, the numbers are the same.")

getBiggerNumber(a, b)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#numberthree(b)

list = []

numbers = (1, -382, 67, 29)
print(numbers)
x = input("Choose the big number from this list:")

def getBiggernumber(x,y):
  if x == 67:
    print("Good. Pick another number.")




getBiggerNumber(numbers)
