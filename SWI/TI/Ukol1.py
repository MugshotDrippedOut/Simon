import random
import time
import matplotlib.pyplot as plt
import numpy as np

"""Pancake sort"""
def pancake_sort(arr, ascending=True):
    def flip(arr, k):
        arr[:k+1] = arr[:k+1][::-1]

    def find_extreme_index(arr, n):
        extreme_idx = 0
        for i in range(n):
            if arr[i] < arr[extreme_idx]:
                extreme_idx = i
        return extreme_idx

    def sort(arr):
        arr = list(arr)
        n = len(arr)
        for curr_size in range(n, 1, -1):
            extreme_index = find_extreme_index(arr, curr_size)

            if extreme_index != curr_size - 1:
                if extreme_index != 0:
                    flip(arr, extreme_index)
                flip(arr, curr_size - 1)
        return tuple(arr)

    sorted_tuple = sort(arr)
    
    if ascending:
        sorted_tuple = sorted_tuple[::-1]

    return sorted_tuple



"""Insertion sort"""
def insertion_sort(arr, ascending=True):
    n = len(arr)
    arr = list(arr)
    compare = lambda a, b: a < b if ascending else a > b

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and compare(key, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    return tuple(arr)
        
        
"""selection sort"""
def selection_sort(arr, ascending=True):
    n = len(arr)
    arr = list(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if (arr[j] < arr[min_idx] and ascending) or (arr[j] > arr[min_idx] and not ascending):
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return tuple(arr)
    

"""Funkcia pre vyisanie sortov"""
def print_all(arr,ascending=True):
    print(pancake_sort(arr,ascending))
    print(insertion_sort(arr,ascending))
    print(selection_sort(arr,ascending))

def time_all(arr,ascending=True):
    print("Pancake sort: ",end="")
    start = time.time()
    pancake_sort(arr,ascending)
    end = time.time()
    print(end - start)
    
    print("Insertion sort: ",end="")
    start = time.time()
    insertion_sort(arr,ascending)
    end = time.time()
    print(end - start)
    
    print("Selection sort: ",end="")
    start = time.time()
    selection_sort(arr,ascending)
    end = time.time()
    print(end - start)
    
"""Random numbers"""
#random_numbers = [random.randint(1,100) for x in range(10)]
#tuple_random_numbers=tuple((random.randint(1, 100), random.randint(1, 100)) for _ in range(1000))

"""
True - ascending
False - descenfing
"""
#print_all(tuple_random_numbers,False)

#time_all(tuple_random_numbers,False)

# generate random numbers
#random_numbers = [random.randint(1, 100) for x in range(10)]
#tuple_random_numbers = tuple((random.randint(1, 100), random.randint(1, 100)) for _ in range(10000))

# sort different sizes of arrays and record the time it takes
sizes = []
for x in range(1, 200, 10):
    sizes.append(x)
pancake_sort_times = []
insertion_sort_times = []
selection_sort_times = []

for size in sizes:
    pancake_sort_time = []
    insertion_sort_time = []
    selection_sort_time = []
    
    for i in range(5):
        arr = [random.randint(1, 100) for x in range(size)]
        
        start = time.perf_counter_ns()
        pancake_sort(arr, False)
        end = time.perf_counter_ns()
        pancake_sort_time.append(end - start)
        
        start = time.perf_counter_ns()
        insertion_sort(arr, False)
        end = time.perf_counter_ns()
        insertion_sort_time.append(end - start)
        
        start = time.perf_counter_ns()
        selection_sort(arr, False)
        end = time.perf_counter_ns()
        selection_sort_time.append(end - start)
    
    pancake_sort_times.append(pancake_sort_time)
    insertion_sort_times.append(insertion_sort_time)
    selection_sort_times.append(selection_sort_time)

print(pancake_sort_times)
print(insertion_sort_times)
print(selection_sort_times)


def create_graph(sort_times, str):
    tests = list(range(1, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(sizes, sort_times, label=tests)
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title(str + 'Sort Algorithm Performance')
    plt.legend()
    
    sort_times_avg = [sum(times) / len(times) for times in sort_times]
    p = np.polyfit(sizes, sort_times_avg, 2)
    curve = np.polyval(p, sizes)
    plt.subplot(2, 1, 2)
    plt.plot(sizes, curve, label='Average')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.subplots_adjust(hspace=0.5)
    plt.show()





create_graph(pancake_sort_times, "Pancake")
create_graph(insertion_sort_times, "Insertion")
create_graph(selection_sort_times, "Selection")