def numerological():
    n = input("Write any name here: ")
    
    output = []
    for char in n.lower():
        if (char != " "):
            num = ord(char) - 96
            output.append(num)
    return sum(output)

print(numerological())
