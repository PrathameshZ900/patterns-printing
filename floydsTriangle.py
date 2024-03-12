# Floyd's Triangle | Printing Numbers in Right Triangle Shape

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

def floydsTri(n):
    cn=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(cn,end=" ")
            cn+=1
        print()    

n=int(input("Inter Your Number: "))
floydsTri(n)