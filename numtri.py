# Printing Numbers in Right Triangle Shape
# type 1
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2
# 1

# type 2
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3 
# 2 2 
# 1

# def typ1(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
# n=int(input("inter your number: "))
# typ1(n)

def typ2(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
n=int(input("inter your number: "))
typ2(n)



