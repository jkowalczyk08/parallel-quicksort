#!/usr/bin/python3
import subprocess
import argparse

parser = argparse.ArgumentParser(description='checks if two files are identical')
parser.add_argument('-g', action='store_true', help="generate input")
parser.add_argument('-t', action='store_true', help="test output")
parser.add_argument('-c', action='store_true', help="clean files")

args = parser.parse_args()

generate = vars(args)['g']
test = vars(args)['t']
clean = vars(args)['c']

if generate:
    subprocess.run('./generate.py', shell=True)

if test:
    subprocess.run('g++ -Wall quicksort.cpp', shell=True)
    subprocess.run('./a.out < small.in > result_small.out', shell=True)
    subprocess.run('./a.out < medium.in > result_medium.out', shell=True)
    subprocess.run('./a.out < large.in > result_large.out', shell=True)
    subprocess.run('./validate.py -c correct_small.out -t result_small.out', shell=True)
    subprocess.run('./validate.py -c correct_medium.out -t result_medium.out', shell=True)
    subprocess.run('./validate.py -c correct_large.out -t result_large.out', shell=True)

if clean:
    subprocess.run('./clean.py', shell=True)