with open("name_code.txt","w") as f:
  f.write("PROGRAMMING IN PYTHON")

with open("name_code.txt","r") as f:
  content = f.read()
print(content)