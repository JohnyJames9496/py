import csv


fields = ["Name", "Branch", "Year", "CGPA"]
rows = [
  ["Nikhil", "CSE", "2","8.0"],
  ["Sanchit", "CSE", "2","9.1",],
  ["Aditya", "IT", "2","9.3"],
  ["Sagar", "IT", "1","9.5"]
]
data = [fields] + rows
with open("people.csv","w",newline="") as file:
  writer = csv.writer(file)
  writer.writerows(data)
  print("Data has been written to people.csv")