def numerical_integration_cython(double a, double b, int n):
    cdef double dx = (b - a) / n
    cdef double result = 0.0
    cdef int i

    for i in range(n):
        x = a + i * dx
        result += x ** 2 * dx

    return result
