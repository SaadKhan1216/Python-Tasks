#Q1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!") 

#Q2
import platform
print(platform.python_version())

#Q3
from datetime import datetime
now=datetime.now()
print (now.strftime("%d-%m-%Y %H:%M:%S"))

#Q4
from math import pi
r=float(input("Input the Radius of Circle: "))
print("Area is: ",pi * r**2)

#Q5
first=str(input("First Name: "))
last= str(input("Last Name: "))
print("Reversed Name is: "+ last +" "+ first)