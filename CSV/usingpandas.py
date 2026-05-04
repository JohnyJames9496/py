import pandas as pd

data = [
    ["John", "CSE", 3, 8.5],
    ["Alice", "ECE", 2, 7.8],
    ["Bob", "ME", 4, 8.2]
]

df = pd.DataFrame(data, columns=["Name", "Branch", "Year", "CGPA"])

df.to_csv("students.csv", index=False)