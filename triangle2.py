#  Printing Stars '*' in Right Angle Triangle Shape

# * * * * *
# * * * *
# * * *
# * * 
# *

def RATshape(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print()
n=int(input("Inter Your Number: "))
RATshape(n)             