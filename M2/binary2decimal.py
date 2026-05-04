def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    
    return binary


# Example
num = 10
print("Binary:", decimal_to_binary(num))