input_str = "malayalam"
d = {}

for char in input_str:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

for key, value in d.items():
    print(key, value)