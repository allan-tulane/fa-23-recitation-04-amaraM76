import random, time
import tabulate


def qsort(a, pivot_fn):
    less = []
    equal = []
    greater = []

    for x in a[1:]:
        if x < pivot_fn:
            less.append(x)
        elif x == pivot_fn:
            equal.append(x)
        else:
            greater.append(x)

    return less, equal, greater
    ## TO DO
    pass
def choose_first_pivot(a):
    return a[0]

def choose_random_pivot(a):
    return random.choice(a)


def ssort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

def tim_sort(list):
    min = 32
    size = len(list)

    for i in range(0, size, min):
        insertion_sort(list[i:i + min])

    
    while min < size:
        for start in range(0, size, 2 * min):
            mid = min((start + min - 1), size - 1)
            end = min((start + 2 * min - 1), size - 1)
            if end > mid:
                merged = list[start:end + 1]
                list[start:start + len(merged)] = merged
        min *= 2

    return list

def insertion_sort(list):
    for i in range(1, len(list)):
        key_item = list[i]
        j = i - 1
        while j >= 0 and list[j] > key_item:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key_item

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 8000, 10000, 20000, 50000, 100000, 200000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = choose_first_pivot
    qsort_random_pivot = choose_random_pivot
    tim_sort1 = tim_sort
    result = []
    for size in sizes:
        mylist_random = list(range(size))
        random.shuffle(mylist_random)

        mylist_sorted = list(range(size))    
        result.append([
            size,
            time_search(qsort_fixed_pivot, mylist_sorted),
            time_search(qsort_random_pivot, mylist_sorted),
            time_search(ssort, mylist_sorted),
            time_search(tim_sort1, mylist_sorted),
            time_search(qsort_fixed_pivot, mylist_random),
            time_search(qsort_random_pivot, mylist_random),
            time_search(ssort, mylist_random),
            time_search(tim_sort1, mylist_random),
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                             headers=['n', 'qsort-fixed-pivot-sorted', 'qsort-random-pivot-sorted', 'ssort-sorted',
                                     'tim_sort-sorted', 'qsort-fixed-pivot-random', 'qsort-random-pivot-random',
                                     'ssort-random', 'tim_sort-random'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
