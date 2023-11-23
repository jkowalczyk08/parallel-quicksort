#!/usr/bin/python3
import subprocess

subprocess.run('g++ -Wall -O3 -o normal.out quicksort.cpp', shell=True)
subprocess.run('g++ -Wall -pthread -O3 -o std_thread.out std_thread_quicksort.cpp', shell=True)
subprocess.run('g++ -Wall -fopenmp -O3 -o openmp.out openmp_quicksort.cpp', shell=True)
