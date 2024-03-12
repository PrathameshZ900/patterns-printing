# Printing Stars in Y Shape

# *           * 
#   *       *   
#     *   *     
#       *       
#       *       
#       *       
#       *       

for i in range(8):
    for j in range(10):
        if (((i<5) and (j == i or j == 8 - i)) or(i>=5 and j==4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

