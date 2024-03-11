# Printing Stars '*' in Pyramid Shape
#     *    
#    * *   
#   * * *  
#  * * * * 
# * * * * *

def triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=" ")
        for i in range(i+1):
            print("*",end=" ")
        print()


n=int(input("Inter Your Number: "))
triangle(n)

