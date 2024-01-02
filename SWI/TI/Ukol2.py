import random
import time
import matplotlib.pyplot as plt
import numpy as np

"""Pancake sort"""
def pancake_sort(arr, ascending=True):
    sorted_tuple = sort(arr)
    
    if ascending:
        sorted_tuple = sorted_tuple[::-1]

    return sorted_tuple


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

def find_extreme_index(arr, n):
    extreme_idx = 0
    for i in range(n):
        if arr[i] < arr[extreme_idx]:
            extreme_idx = i
    return extreme_idx

def flip(arr, k):
    arr[:k+1] = arr[:k+1][::-1]

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
    
"""Funkcia pre meranie casov"""
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

    
"""Testovacie pole"""
def get_sort_times(sizes, cycles, case="average"):
    pancake_sort_times = []
    insertion_sort_times = []
    selection_sort_times = []

    for size in sizes:
        pancake_sort_time = []
        insertion_sort_time = []
        selection_sort_time = []

        for i in range(cycles):
            if case =="average":
                arr = [random.randint(1, 1000) for x in range(size)]
            elif case =="best":
                arr = [x for x in range(size)]
            elif case =="worst":
                arr = [x for x in range(size,0,-1)]

            start = time.perf_counter_ns()
            pancake_sort(arr)
            end = time.perf_counter_ns()
            pancake_sort_time.append(end - start)

            start = time.perf_counter_ns()
            insertion_sort(arr)
            end = time.perf_counter_ns()
            insertion_sort_time.append(end - start)

            start = time.perf_counter_ns()
            selection_sort(arr)
            end = time.perf_counter_ns()
            selection_sort_time.append(end - start)

        pancake_sort_times.append(pancake_sort_time)
        insertion_sort_times.append(insertion_sort_time)
        selection_sort_times.append(selection_sort_time)

    return pancake_sort_times, insertion_sort_times, selection_sort_times


"""Funkcia pre získanie kriviek"""
def get_sort_curves(sizes, sort_times_best, sort_times_avg, sort_times_worst):
    sort_times_avg_curve = np.polyval(np.polyfit(sizes, [sum(times) / len(times) for times in sort_times_avg], 2), sizes)
    sort_times_best_curve = np.polyval(np.polyfit(sizes, [sum(times) / len(times) for times in sort_times_best], 2), sizes)
    sort_times_worst_curve = np.polyval(np.polyfit(sizes, [sum(times) / len(times) for times in sort_times_worst], 2), sizes)
    
    return sort_times_best_curve, sort_times_avg_curve, sort_times_worst_curve


"""Funkcia pre vykreslenie grafov"""
def create_graph(sort_times,sort_times_best, sort_times_worst, str):
    #tests = list(range(1, 6))
    curve_best, curve, curve_worst = get_sort_curves(sizes, sort_times_best, sort_times, sort_times_worst) 
    
    plt.subplot(2, 1, 1)
    plt.plot(sizes, sort_times,linewidth=.5, mew=0, alpha=0.7)
    plt.plot(sizes, curve, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel('Array Size')
    plt.ylabel('Time (ns)')
    plt.title(str + ' Sort Algorithm Performance')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(sizes, curve_best, label='Best',linewidth=1, color='g',alpha=0.7)
    plt.plot(sizes, curve, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.plot(sizes, curve_worst, label='Worst',linewidth=1, color='r',alpha=0.7)
    plt.xlabel('Array Size')
    plt.ylabel('Time (ns)')
    plt.title(str + ' Sort Algorithm Performance')
    plt.legend()
    plt.subplots_adjust(hspace=0.5)

    
    plt.show()

    

#print(pancake_sort_times)
#print(insertion_sort_times)
#print(selection_sort_times)



if __name__ == '__main__':
    cycles = 10 #pocet cyklov
    sizes = [] #velkosti poli
    for x in range(1, 1000, 10):
        sizes.append(x) 
    pancake_sort_times, insertion_sort_times, selection_sort_times = get_sort_times(sizes,cycles)
    pancake_sort_times_best, insertion_sort_times_best, selection_sort_times_best = get_sort_times(sizes,cycles,"best")
    pancake_sort_times_worst, insertion_sort_times_worst, selection_sort_times_worst = get_sort_times(sizes,cycles,"worst")

    """Vykreslenie grafov"""
    create_graph(pancake_sort_times, pancake_sort_times_best, pancake_sort_times_worst, "Pancake")
    create_graph(insertion_sort_times, insertion_sort_times_best, insertion_sort_times_worst, "Insertion")
    create_graph(selection_sort_times, selection_sort_times_best, selection_sort_times_worst, "Selection")
