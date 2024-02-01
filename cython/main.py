# main.py
from sum_of_squares import numerical_integration_python as sum_of_squares_python
from sum_of_squares_cython import numerical_integration_cython
import time

# Python implementation
start_time_python = time.time()
result_python = sum_of_squares_python(0, 1, 100000000)
end_time_python = time.time()
print(f"Python Result: {result_python}")
print(f"Python Execution Time: {end_time_python - start_time_python:.6f} seconds")

# # Cython implementation
# start_time_cython = time.time()
# result_cython = numerical_integration_cython(0, 1, 100000000)
# end_time_cython = time.time()
# print(f"Cython Result: {result_cython}")
# print(f"Cython Execution Time: {end_time_cython - start_time_cython:.6f} seconds")
