# Printing Stars '*' in N Shape
# *       *
# * *     *
# *  *    *
# *   *   *
# *     * *


for i in range(5):
    for j in range(5):
        if ( i==j or j==0 or j==4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
