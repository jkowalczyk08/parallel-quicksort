#!/usr/bin/python3
import subprocess

subprocess.run('./build.py', shell=True)

print('testing normal')
for i in range(1, 6):
    subprocess.run(f'./normal.out 0 < test_cases/{i}.in > test_cases/{i}result.out', shell=True)
    subprocess.run(f'./validate.py -c test_cases/{i}.out -t test_cases/{i}result.out', shell=True)

print('testing std::thread')
for i in range(1, 6):
    subprocess.run(f'./std_thread.out 0 4 < test_cases/{i}.in > test_cases/{i}result.out', shell=True)
    subprocess.run(f'./validate.py -c test_cases/{i}.out -t test_cases/{i}result.out', shell=True)

print('testing openmp')
for i in range(1, 6):
    subprocess.run(f'./openmp.out 0 16 < test_cases/{i}.in > test_cases/{i}result.out', shell=True)
    subprocess.run(f'./validate.py -c test_cases/{i}.out -t test_cases/{i}result.out', shell=True)

