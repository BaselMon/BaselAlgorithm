import time

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

n = int(input())
start_time = time.time()
result = fact(n)
print(result)
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print("Execution time:", execution_time, "milliseconds")
