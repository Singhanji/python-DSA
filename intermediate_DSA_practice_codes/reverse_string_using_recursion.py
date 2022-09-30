def main():
    n = input()
    if len(n) == 1:
        return n
    
    res = n[::-1]
    return res

print(main())


