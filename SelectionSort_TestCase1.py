from random import randint, random
from SelectionSort import selectionsort
from time import time

 
averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_SelectionWorst():
    start= time()
    assert selectionsort(worstcase) == bestcase
    print(time()-start)
 
def test_SelectionBest():
    start= time()
    assert selectionsort(bestcase) == bestcase
    print(time()-start)
 
def test_SelectionAvg():
    start= time()
    assert selectionsort(averagecase) == bestcase
    print(time()-start)


import matplotlib.pyplot