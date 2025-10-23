def nod(a,b):
    if b == 0:
        return abs(a)
    return nod(b, a % b)
