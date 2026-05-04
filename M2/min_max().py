def min_max(n):
    smallest = n[0]
    largest = n[0]

    for num in n:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest

n = [1, 67, 343, 12, 99]
small, large = min_max(n)

print("Smallest:", small)
print("Largest:", large)