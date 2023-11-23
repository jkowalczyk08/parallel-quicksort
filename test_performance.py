#!/usr/bin/python3
import subprocess

max_depth = 4 # number of threads in std_thread version is 2^max_depth
cores_num = 8
openmp_threads = 16

subprocess.run('./build.py', shell=True)

print('testing normal')
for i in range(1, 9):
    subprocess.run(f'./normal.out 1 < test_cases/{i}.in', shell=True)

print(f'testing std::thread with {pow(2, max_depth)} threads')
for i in range(1, 9):
    subprocess.run(f'taskset -c 1-{cores_num} ./std_thread.out 1 {max_depth} < test_cases/{i}.in', shell=True)

print(f'testing openmp with {openmp_threads} threads')
for i in range(1, 9):
    subprocess.run(f'taskset -c 1-{cores_num} ./openmp.out 1 {openmp_threads} < test_cases/{i}.in', shell=True)

