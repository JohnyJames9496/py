d = {
    "johny": "16/11/2004",
    "bibin": "27/03/2004",
    "alan": "9/05/2004",
    "kunjumon": "5/01/2004",
    "binoy":"28/03/2004"
}

name = input("Enter the name: ").lower()

if name in d:
    print("Birthday:", d[name])
else:
    print("Name not found")