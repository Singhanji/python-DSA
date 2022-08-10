def to_lower(A):
    
    r = ""
    for k, v in enumerate(A):
        v = v.lower()
        r += f" {v}"

    return r.strip()

A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
print(to_lower(A))
