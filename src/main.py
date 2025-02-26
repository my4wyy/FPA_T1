def karatsuba(x: int, y: int) -> int:
    """
    Multiplica dois inteiros usando o algoritmo de Karatsuba.
    """
    if min(x, y) < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2  
    
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)
    
    p1 = karatsuba(low_x, low_y)
    p2 = karatsuba(high_x, high_y)
    p3 = karatsuba(low_x + high_x, low_y + high_y)
    
    return (p2 * 10**(2 * m)) + ((p3 - p2 - p1) * 10**m) + p1

if __name__ == "__main__":
    a, b = 2807, 2005
    resultado = karatsuba(a, b)
    print(f"{a} * {b} = {resultado}")
