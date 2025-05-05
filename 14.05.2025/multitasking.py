import multiprocessing
import time
from colorama import Fore, init
init(autoreset=True)

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        print(i)
        print(result)
        result *= i
        print(' ')
    return result

def factorials_in_parallel(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_factorial, numbers)
    return results 

if __name__ == '__main__':
    numbers = list(range(1, 10))
    start_time = time.time()
    results_parallel = factorials_in_parallel(numbers)
    end_time = time.time()
    parallel_time = end_time - start_time

    print(Fore.GREEN + f'Time with multiprocessing: {parallel_time:.4f} secs')

    start_time = time.time()
    results_seq = [calculate_factorial(n) for n in numbers]
    end_time = time.time()
    seq_time = end_time - start_time

    print(Fore.GREEN + f'Time without multiprocessing: {seq_time:.4f} secs') 

    print(Fore.GREEN + f'First 5 multiprocessing results: {results_parallel[:5]}')
    print(Fore.GREEN + f'First 5 without multiprocessing results: {results_seq[:5]}')