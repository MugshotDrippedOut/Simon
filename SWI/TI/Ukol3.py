import random
import sys
import time
import math
import matplotlib.pyplot as plt
import numpy as np


sys.setrecursionlimit(1000000)#maximalny pocet rekurzii
sys.set_int_max_str_digits(1000000)#maximalny pocet cifier 



"""Funkcia pre výpočet faktoriálu pomocou rekurzie a cyklu"""
def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""Funkcia pre výpočet Fibonacciho postupnosti pomocou rekurzie a cyklu"""
def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b


"""Funkcia insertion sort pre triedenie zoznamu pomocou rekurzie a cyklu"""
def insertion_sort_rec(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    else:
        insertion_sort_rec(arr, n - 1)
        key = arr[n - 1]
        j = n - 2

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        return arr


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

"""Funkcia quick sort pre triedenie zoznamu pomocou rekurzie a cyklu"""
def quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot = arr[start]
        left = start + 1
        right = end
        while left <= right:
            if arr[left] <= pivot:
                left += 1
            elif arr[right] > pivot:
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[start], arr[right] = arr[right], arr[start]
        stack.append((start, right - 1))
        stack.append((right + 1, end))
    return arr


def quick_sort_rec(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_rec(less) + [pivot] + quick_sort_rec(greater)

    

"""Funkcia pre ziskanie casu pre jednotlive velkosti vstupu"""
def get_times(sizes, func, loops=10, sort=False):
    function_times = []
    for size in sizes:
        function_time = []
        for i in range(loops):
            if sort:
                arr = [random.randint(0, 10000) for x in range(size)]
                start = time.perf_counter_ns()
                func(arr)
                end = time.perf_counter_ns()
                function_time.append(end - start)
                continue
            start = time.perf_counter_ns()
            func(size)
            end = time.perf_counter_ns()
            function_time.append(end - start)
        function_times.append(function_time)
    return function_times


"""Funkcia pre vypocet priemeru casu"""
def get_avg_time(times):
    return sum(times) / len(times)



"""Funkcia pre konverziu nanosekund na sekundy"""
def convert_ns_to_s(times):
    for i in range(len(times)):
        for j in range(len(times[i])):
            times[i][j] /= 1000000000
    return times


"""Funckia pre vypocet priemerovej krivky"""
def get_avg_curve(sizes, times):
    return np.polyval(np.polyfit(sizes, [get_avg_time(time) for time in times], 2), sizes)


"""Funkcia pre vytvorenie grafu"""
def create_plot(sizes, times, func_name ):
    times = convert_ns_to_s(times)
    avg = get_avg_curve(sizes, times)
    plt.plot(sizes, times, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name)
    plt.legend()


"""Funckia pre vytvorenie dvoch grafov"""
def create_plot_2(sizes, times, times_rec, func_name, func_name_rec):
    times = convert_ns_to_s(times)
    times_rec = convert_ns_to_s(times_rec)
    avg = get_avg_curve(sizes, times)
    avg_rec = get_avg_curve(sizes, times_rec)
    plt.subplot(2, 1, 1)
    plt.plot(sizes, times, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(sizes, times_rec, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg_rec, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name_rec)
    plt.show()




"""Funckia pre vytvorenie dvoch grafov"""
def create_plot_2_avg(sizes, times, times_rec, func_name, func_name_rec):
    times = convert_ns_to_s(times)
    times_rec = convert_ns_to_s(times_rec)
    avg = get_avg_curve(sizes, times)
    avg_rec = get_avg_curve(sizes, times_rec)
    plt.subplot(2, 2, 1)
    plt.plot(sizes, times, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name)
    plt.legend()
    
    plt.subplot(2, 2, 2)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(sizes, times_rec, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg_rec, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name_rec)
    
    plt.subplot(2, 2, 3)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(sizes, avg, label=func_name,linewidth=1, color='b',alpha=0.7)
    plt.plot(sizes, avg_rec, label=func_name_rec,linewidth=1, color='g',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name + " and " + func_name_rec)
    plt.legend()
    plt.show()


"""Funkcia pre vytvorenie troch grafov a jedneho grafu s priemernymi krivkami"""
def create_plot_3_avg(sizes, times_1, times_2, times_3, func_name_1, func_name_2, func_name_3):
    times_1 = convert_ns_to_s(times_1)
    times_2 = convert_ns_to_s(times_2)
    times_3 = convert_ns_to_s(times_3)
    avg_1 = get_avg_curve(sizes, times_1)
    avg_2 = get_avg_curve(sizes, times_2)
    avg_3 = get_avg_curve(sizes, times_3)
    
    plt.subplot(2, 2, 1)
    plt.plot(sizes, times_1, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg_1, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name_1)
    plt.legend()
    
    plt.subplot(2, 2, 2)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(sizes, times_2, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg_2, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name_2)
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(sizes, times_3, linewidth=.7, mew=0, alpha=0.7)
    plt.plot(sizes, avg_3, label='Average',linewidth=1, color='b',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name_3)
    plt.legend()
    
    plt.subplot(2, 2, 4)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(sizes, avg_1, label=func_name_1,linewidth=1, color='b',alpha=0.7)
    plt.plot(sizes, avg_2, label=func_name_2,linewidth=1, color='g',alpha=0.7)
    plt.plot(sizes, avg_3, label=func_name_3,linewidth=1, color='r',alpha=0.7)
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.title("Time complexity of " + func_name_1 + ", " + func_name_2 + " and " + func_name_3)
    plt.legend()
    
    plt.show()
    
def generate_list( size, jump):
    arr=[]
    for i in range(1,size,jump):
        arr.append(i)
    return arr




if __name__=="__main__":
    loops = 5

    sizes_factorial = generate_list( 2000, 100)
    sizes_fibbonaci = generate_list( 30, 1) 
    sizes_insertion_sort = generate_list( 500, 50)
    sizes_quick_sort = generate_list( 4000, 400)
    #print(len(str(factorial_rec(1000))))
    #print(len(str((factorial(100000)))))
    #print(math.factorial(100000) ==factorial_rec(100000))
        
    #print(get_times(sizes_factorial, factorial_rec, 10))
    #print(get_times(sizes_factorial, fibonacci, 10))
    #print(get_times(sizes_factorial, insertion_sort_rec, 10, True))
    
    create_plot_3_avg(sizes_factorial, get_times(sizes_factorial, factorial, loops),
                  get_times(sizes_factorial, factorial_rec, loops), 
                  get_times(sizes_factorial, math.factorial, loops), 
                  "Factorial", "Recursive Factorial", "Factorial from math library")
    create_plot_2_avg(sizes_fibbonaci, get_times(sizes_fibbonaci, fibonacci, loops),
                  get_times(sizes_fibbonaci, fibonacci_rec, loops), 
                  "Fibonacci", "Recursive Fibonacci")
    create_plot_2_avg(sizes_insertion_sort, get_times(sizes_insertion_sort, insertion_sort, loops, True),
                  get_times(sizes_insertion_sort, insertion_sort_rec, loops, True), 
                  "Insertion Sort", "Recursive Insertion Sort")
    create_plot_2_avg(sizes_quick_sort, get_times(sizes_quick_sort, quick_sort, loops, True),
                  get_times(sizes_quick_sort, quick_sort_rec, loops, True), 
                  "Quick Sort", "Recursive Quick Sort")