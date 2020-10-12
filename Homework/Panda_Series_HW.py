## Author: Cameron Collier
## Date: 10/10/2020
## Program Name: Panda Series Homework

import pandas as pd 
import numpy as np

## create series from list
list_series = pd.Series([7, 11, 13, 17])

## create series with 5 values of 100
hundred_series = pd.Series(100, range(5))

## create a series randomly in the range 0-100 with a size of 20
random_series = pd.Series(np.random.randint(0,101, size=20))

## create a series for temperatures and use an index
temperatures = pd.Series([98.6, 98.9, 100.2,97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])

## create a series from a dictionary using the same values as temperatures above
temps_dict = {'Julie':98.6, 'Charlies':98.9, 'Sam':100.2, 'Andrea':97.9}
temps_dict_series = pd.Series(temps_dict)


## print list series
print("\nLIST SERIES:")
print(list_series)

## print hundred series
print("\nHUNDRED SERIES:")
print(hundred_series)

## print random series
print("\nRANDOM SERIES:")
print(random_series.describe())

## print temperatures series
print("\nTEMPERATURES:")
print(temperatures)

## print temps dict series
print("\nTEMPS FROM DICT SERIES:")
print(temps_dict_series)