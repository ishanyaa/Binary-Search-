Bubble Sort Algorithm README
This repository contains a Python implementation of the Bubble Sort algorithm, along with a demonstration of its usage to sort a list of random numbers.

Bubble Sort Overview
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. Although Bubble Sort is not efficient for large lists, it provides a straightforward example of a sorting algorithm and is often used for educational purposes.

Implementation Details
The bubble_sort function defined in bubble_sort.py takes an input list and sorts it using the Bubble Sort algorithm. The implementation consists of the following steps:

Initialize a variable swapped to True.
Enter a loop that continues as long as swapped is True.
Inside the loop, set swapped to False.
Iterate through the list using a for loop from the first element to the second-to-last element.
If the current element is greater than the next element, swap them and set swapped to True.
After completing a pass through the list, increment the iterations counter.
If no swaps were made during a pass, swapped remains False, and the loop exits.
Return the sorted list and the number of iterations.
Usage
To use the Bubble Sort implementation, follow these steps:

Make sure you have Python installed on your system.
Download or clone this repository to your local machine.
Open a terminal or command prompt and navigate to the repository's directory.
Run the bubble_sort.py script by executing the command: python bubble_sort.py
The script generates a list of random numbers, applies the Bubble Sort algorithm to sort the list, and prints the original list, the sorted list, and the number of iterations required to sort the list.




Contributing
If you would like to contribute to this project by improving the Bubble Sort implementation or adding more sorting algorithms, feel free to fork this repository and submit a pull request with your changes.
