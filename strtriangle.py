# Printing Strings in Right Triangle Shape
# p
# p y
# p y t 
# p y t h 
# p y t h o
# p y t h o n

def strtri(s,n):
    for i in range(n):
        for j in range(i+1):
            print(s[j],end=" ")
        print()    
s=input("input your str:")
n=len(s)
strtri(s,n)
