# Printing Stars in X Shape
# *       * 
#   *   *   
#     *     
#   *   *   
# *       *



size = 5
for i in range(size):
    for j in range(size):
        if j == i or j == size - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()