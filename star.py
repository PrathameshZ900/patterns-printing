# Printing Stars '*' in Right Angle Triangle Shape

def rightAngle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()


# it will give you 
# *
# * *
# * * *
# * * * *
n=int(input("Inter Your Number: "))
rightAngle(n)