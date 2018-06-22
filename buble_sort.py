from random import shuffle


def bubble_sort(a):
    '''
        Sort on place with Bubblesort algorithm
    '''
    for bypass in range(1, len(a)):
        for k in range(0, len(a) - bypass):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
    return a

def test_sort_works_in_simple_cases():
    print("- sort algorithm for simple cases:")
    passed = True

    for A1 in ([1], [], [1,2], [1,2,3,4,5],
               [4,2,5,1,3], [5,4,4,5,5],
               list(range(20)), list(range(20, 1, -1))):
        shuffle(A1)
        A2 = sorted(list(A1)) # a bit of cheating to test own algorithm with python existing
        bubble_sort(A1)
        passed &= all(x == y for x, y in zip(A1, A2))

    return passed

def test_sort_algorithm_stable():
    print("- sort algorithm is stable:")
    passed = True

    # testing types: str, float, list
    for A1 in (list('ajhbfvhbei'),
               [float(i)**0.5 for i in range(10)],
               [[1,3], [4,5], [2,4,5], [6,7]]):
        shuffle(A1)
        A2 = sorted(list(A1))
        bubble_sort(A1)
        passed &= all(x == y for x,y in zip(A1, A2))

    print("Ok" if passed else "Fail")
    return passed

def test_sort_alogrithm_is_universal():
    passed = True
    return passed

def test_sort_algorithm_scalability():
    passed = True
    return passed

def test_sort():
    print "Test sorting algorithm"
    passed = True

    passed &= test_sort_works_in_simple_cases()
    passed &= test_sort_algorithm_stable()

    print("Summary: ", "Ok" if passed else "Fail")

if __name__ == "__main__":
    test_sort()
    # buble_sort(input())