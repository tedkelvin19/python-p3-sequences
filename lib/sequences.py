#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_series = []
    if length == 0:
        fibonacci_series = []
    elif length == 1:
        fibonacci_series = [0]
    elif length == 2:
        fibonacci_series = [0, 1]
    else:
        fibonacci_series = [0, 1]
        for i in range(2, length):
            fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
    print(fibonacci_series)
print_fibonacci(9)        