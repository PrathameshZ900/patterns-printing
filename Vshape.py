# Printing Stars in V Shape
# *           *
#   *       *
#     *   *
#       *

for i in range(5):
    for j in range(10):
        if j == i or j == 8 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

