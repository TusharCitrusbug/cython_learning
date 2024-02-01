import myModule.module1 as module1
all_attributes = dir(object)
c=callable(object)
print(c)
# Filter out methods
# methods = [attribute for attribute in all_attributes if callable(getattr(object, attribute))]

# # Print the list of methods
# print("Number of methods:", len(methods))
# print("List of methods:", methods)
# print(module1.__spec__.loader)
# import threading
# import time
# print("called 11111111111")
# # A simple CPU-bound function
# def cpu_bound_task():
#     count = 0
#     for _ in range(10**7):
#         count += 1

# # Function to measure the time taken to execute a CPU-bound task using threads
# def measure_time_using_threads():
#     start_time = time.time()

#     # Create two threads to run the CPU-bound task concurrently
#     thread1 = threading.Thread(target=cpu_bound_task)
#     thread2 = threading.Thread(target=cpu_bound_task)

#     # Start the threads
#     thread1.start()
#     thread2.start()

#     # Wait for both threads to finish
#     thread1.join()
#     thread2.join()

#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"Time taken using threads: {elapsed_time} seconds")

# # Function to measure the time taken to execute a CPU-bound task using multiprocessing
# def measure_time_using_multiprocessing():
#     from multiprocessing import Process

#     start_time = time.time()

#     # Create two processes to run the CPU-bound task concurrently
#     process1 = Process(target=cpu_bound_task)
#     process2 = Process(target=cpu_bound_task)

#     # Start the processes
#     process1.start()
#     process2.start()

#     # Wait for both processes to finish
#     process1.join()
#     process2.join()

#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"Time taken using multiprocessing: {elapsed_time} seconds")

# if __name__ == "__main__":
#     print("called 2222222222222222222")

#     print("Using threads:")
#     measure_time_using_threads()

#     print("\nUsing multiprocessing:")
#     measure_time_using_multiprocessing()
