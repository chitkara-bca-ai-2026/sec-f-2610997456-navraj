n = int(input("enter number of rows: "))

print("\n========== pattern 1: star triangle ==========")

for row in range(1, n + 1):
    print("* " * row)

print("\n========== pattern 2: number triangle ==========")

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

print("\n======= pattern 3: inverted star triangle =======")

for row in range(n, 0, -1):
    print("* " * row)

print("\n============ pattern 4: pyramid ============")

for row in range(1, n + 1):
    print(" " * (n - row) + "* " * row)