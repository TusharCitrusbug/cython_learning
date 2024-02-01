def numerical_integration_python(a, b, n):
    dx = (b - a) / n
    result = 0.0
    for i in range(n):
        x = a + i * dx
        result += x ** 2 * dx
    return result