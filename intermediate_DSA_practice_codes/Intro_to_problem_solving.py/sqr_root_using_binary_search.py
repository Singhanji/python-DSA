def solve(A):
    low = 0
    high = A
    while(low<=high):
        mid = (low + high) // 2
        m_s = mid * mid
        if m_s <= A:
            low = mid + 1
        else:
            high = mid - 1
        if m_s == A:
            return mid
    return -1
    


A = 25
print(solve(A))