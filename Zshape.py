# Printing Stars in Z Shape

# * * * * * * * 
#           * 
#         *   
#       *     
#     *       
#   *         
# * * * * * * * 

size = 7
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == size - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

