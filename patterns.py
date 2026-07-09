# 1.
# square
for row in range(1,5):
    for col in range(1,5):
            print("*", end=" ")
    print()

# 2.
# right angle triangle
height=5
for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# 3.
# pyramid
height=5
for i in range(1, height + 1):

        # Print spaces
        for j in range(height - i):
            print(" ", end="")

        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")

        print()