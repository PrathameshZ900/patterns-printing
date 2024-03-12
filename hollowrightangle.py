# Printing Stars in Hollow Right Triangle Shape


# * * * * *
#   *     *
#     *   *
#       * *
#         *

def hollowRt(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==n-1 or i==j):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

n=int(input("Inter Your Number: "))
hollowRt(n)
                    