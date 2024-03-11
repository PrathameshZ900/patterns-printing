# Printing Stars '*' in I Shape
# *
# *
# *
# *
# *
# *
# * * * * *

for i in range(7):
    for j in range(5):
        if  i == 6 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
