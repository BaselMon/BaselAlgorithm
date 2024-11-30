import time

n = int(input("Enter a number: "))

start_time = time.time()

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n}: {factorial}")

end_time = time.time()
execution_time = (end_time - start_time) * 1000

print("Execution time:", execution_time, "milliseconds")
