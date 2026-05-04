with open("numbers.txt", "r") as f:
    content = f.read()


numbers = list(map(int, content.split()))


numbers.sort()

n = len(numbers)

if n % 2 == 0:
    mid = n // 2
    median = (numbers[mid - 1] + numbers[mid]) / 2
else:
    mid = n // 2
    median = numbers[mid]

print("Median:", median)