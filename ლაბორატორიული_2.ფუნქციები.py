import math
import random
print("დავალება---1")
number = float(input("შეიყვანეთ რიცხვი: "))

r = round(number,1)
f = math.floor(number)
c = math.ceil(number)
t = math.trunc(number)
print(r)
print(f)
print(c)
print(t)
print("დავალება---2")
number1 = float(input("რიცხვი 1: "))
number2 = float(input("რიცხვი 2: "))
number3 = float(input("რიცხვი 3: "))
m = max(number1,number2,number3)
print("სამ რიცხვს შორის მაქსიმალური არის: ",m)
import math
print("დავალება---3")
def cal():
  print(math.pow(3, 8))
  print(math.pow(2, 9))
  print(math.pow(4, 6))
cal()
print("დავალება---4")
def square():
    print(math.sqrt(225625))
    print(math.sqrt(4225))
square()
print("დავალება---5")
r = round(random.uniform(0,1),3)
print(r)
print("დავალება---6")
r = round(random.uniform(100,120),1)
print(r)
print("დავალება---8")
def avg(num1,num2):
  return (num1+num2)/2
for number1 in range(1):
  for number2 in range(3):
    number1 = int(input("pirceli ricxvi: "))
    number2 = int(input("meore ricxvi: "))
    print(avg(number1,number2))
print("დავალება---9")
def avg(num1,num2):
  a = (num1+num2)/2
  print(a)
for number1 in range(1):
  for number2 in range(3):
    number1 = int(input("pirceli ricxvi: "))
    number2 = int(input("meore ricxvi: "))
    avg(number1,number2)
print("დავალება---10")
def avg(num):
  return num**3
for number in range(3):
  number = int(input("ricxvi: "))
  print(avg(number))
print("დავალება---11")
def minimum(num1,num2):
  return min(num1,num2)
number1 = int(input("pirceli ricxvi: "))
number2 = int(input("meore ricxvi: "))
print(minimum(number1,number2))
print("დავალება---12")
def odd(num):
  if num%2!=0:
    print(True)
  else:
    print(False)
for number in range(3):
  number = int(input("mteli ricxvi: "))
  odd(number)
print("დავალება---13")
def fact(num):
  factorial = 1
  if num < 0:
    return "Sorry, factorial does not exist for negative numbers"
  elif num == 0:
    return "The factorial of 0 is 1"
  else:
    for i in range(1,num + 1):
      factorial = factorial*i
    return factorial
for number in range(3):
  number = int(input("mteli ricxvi: "))
  print("Factorial: ",fact(number))
print("დავალება---15")
def hello_world():
  print("Hello World")
hello_world()
print("დავალება---16")
num = int(input("Sheiyvanet ricxvi: "))
x = lambda x:x**3
print(x(num))















