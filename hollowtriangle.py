# Printing Stars in Hollow Equilateral Triangle Shape | Pyramid Pattern
#     *   
#   *   *
# *   *    *

# for i in range(1,5):
#     for j in range(1,8):
#         if(i==4 or i+j==5 or j-i==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
                
def solve(n):
    for i in range(1,n+1):
        for j in range(1,n*2):
            if(i==n or i+j==n+1 or j-i == n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n=int(input("Inter Number here: "))
solve(n)
                
