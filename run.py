#!/usr/bin/python3
import subprocess
import argparse

def validate_one_impl():
    subprocess.run('./validate.py -c correct_small.out -t result_small.out', shell=True)
    subprocess.run('./validate.py -c correct_medium.out -t result_medium.out', shell=True)
    subprocess.run('./validate.py -c correct_large.out -t result_large.out', shell=True)

parser = argparse.ArgumentParser(description='checks if two files are identical')
parser.add_argument('-v', action='store_true', help="validate output")
parser.add_argument('-r', action='store_true', help="run implementations")

args = parser.parse_args()

validate = vars(args)['v']
run = vars(args)['r']

if run:



if validate:
    print('Validating simple implementation')
    subprocess.run('g++ -Wall -O3 quicksort.cpp', shell=True)
    subprocess.run('./a.out < small.in > result_small.out', shell=True)
    subprocess.run('./a.out < medium.in > result_medium.out', shell=True)
    subprocess.run('./a.out < large.in > result_large.out', shell=True)
    validate_one_impl()

    print('Testing std::thread implementation')
    subprocess.run('g++ -Wall -pthread -O3 std_thread_quicksort.cpp', shell=True)
    depth = 4
    subprocess.run(f'./a.out {depth} < small.in > result_small.out', shell=True)
    subprocess.run(f'./a.out {depth} < medium.in > result_medium.out', shell=True)
    subprocess.run(f'./a.out {depth} < large.in > result_large.out', shell=True)
    validate_one_impl()