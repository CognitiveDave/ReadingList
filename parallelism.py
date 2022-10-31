#!/usr/bin/env python
# coding: utf-8

# ## Demonstration of multi-processing


import pandas as pd
from datetime import datetime
import multiprocessing
import time
from multiprocessing import Pool

#The work to be done

#load 5 copies of a very large file
path = "/home/david/Downloads/"
file = "companies_sorted.csv"
filePath = path+file

work = [filePath,filePath,filePath,filePath,filePath,filePath, filePath, filePath, filePath,filePath,filePath, filePath, filePath, filePath,filePath,filePath, filePath, filePath, filePath,filePath,filePath, filePath, filePath, filePath]
frames = []



def worktodo(file):
    df = pd.read_csv(file)
    df=df.groupby('size range').agg({'year founded': ['min', 'max', 'count'], 'country': lambda x: x.nunique(), 'current employee estimate': 'median'}).reset_index()
    cols = ['size range','min year','max year','count','country','employee estimate']
    df.columns=cols
    return df



def summary(frames):
    frame = pd.concat(frames)
    print(frame.shape)  
    print(frame.groupby('size range').agg({'min year': 'min', 'max year': 'max', 'count': 'mean','employee estimate': 'mean', 'country': 'mean'}))
    print(" ")



def singleCpu():
    start_time = time.perf_counter()

    frames = []
    for todo in work:
        frames.append(worktodo(todo))

    summary(frames)
    
    finish_time = time.perf_counter()

    print(f"Program finished in {finish_time-start_time} seconds")
    
    del frames
    


if __name__ == "__main__":
    print ("-->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print (f"work to be done: {len(work)}")
    print ("<------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    singleCpu()
    start_time = time.perf_counter()

    with Pool() as mp_pool:
        results = mp_pool.map(worktodo, work)
        
      
    summary(results)
    
    finish_time = time.perf_counter()
 
    print(f"Program finished in {finish_time-start_time} seconds")
    

