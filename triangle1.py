#  Printing Stars '*' in Reverse Pyramid Shape
# * * * * * 
#  * * * * 
#   * * *  
#    * *   
#     *  

def triangleRev(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")    
        print()
n=int(input("Inter Your Number: "))
triangleRev(n)  