# Printing Stars '*' in T Shape
# * * * * *
#     *
#     *
#     *
#     *
#     *
#     * 

for i in range(7):
    for j in range(5):
        if i == 0 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
