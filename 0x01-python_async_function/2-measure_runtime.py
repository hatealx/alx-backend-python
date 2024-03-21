#!/usr/bin/env python3
"""
<----- Measure Runtime ----->
"""
import time

# Import wait_n from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay) and return the average time per call."""
    start = time.time()
    for _ in range(n):
        wait_n(n, max_delay)  # Call wait_n function
    end = time.time()

    total_time = end - start
    return total_time / n
