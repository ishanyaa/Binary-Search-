#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

def bubble_sort(arr):
    n = len(arr)
    iterations = 0
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:


                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        iterations += 1

    return arr, iterations

def main():
    num_count = 25
    random_numbers = [random.randint(1, 10000000000) for _ in range(num_count)]

    print("Original List:", random_numbers)

    sorted_numbers, iterations_needed = bubble_sort(random_numbers.copy())
    print("Sorted List:", sorted_numbers)
    print("Iterations needed:", iterations_needed)

if __name__ == "__main__":
    main()


# In[ ]:




