from random import randint, random
from InsertionSort import insertion_Sort
from time import time
 
averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_InsertionWorst():
    start= time()
    assert insertion_Sort(worstcase) == bestcase
    print(time()-start)
 
def test_InsertionBest():
    start= time()
    assert insertion_Sort(bestcase) == bestcase
    print(time()-start)
 
def test_InsertionAvg():
    start= time()
    assert insertion_Sort(averagecase) == bestcase
    print(time()-start)


import matplotlib.pyplot