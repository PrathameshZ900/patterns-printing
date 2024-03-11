#  Printing Stars '*' in Right Angle Odd Triangle Shape
# *
# * * *              
# * * * * *         n=12 or 11
# * * * * * * *
# * * * * * * * * *
# * * * * * * * * * * *

def rightOddAngle(n):
    for i in range(1,n+1):
        if(i%2==1):
            for i in range(1,i+1):
                print("*",end=" ")
            print()


n=int(input("Inter Your Number: "))
rightOddAngle(n)