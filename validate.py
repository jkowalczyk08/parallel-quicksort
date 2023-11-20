#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='checks if two files are identical')
parser.add_argument('-c', '--correct-output', help='name of correct output file', required=True)
parser.add_argument('-t', '--tested-output', help='name of tested output file', required=True)

args = parser.parse_args()
correct = vars(args)['correct_output']
tested = vars(args)['tested_output']

print(f'comparing {correct} with {tested}')

i = 0
identical = True
with open(correct) as f1:
    with open(tested) as f2:
        f1_data = f1.readlines()
        f2_data = f2.readlines()
        
        for (f1_line, f2_line) in zip(f1_data, f2_data):
            if f1_line != f2_line:
                print("Line ", i, ":")
                print("\tFile 1:", f1_line)
                print("\tFile 2:", f2_line)
                identical = False
            i += 1

        if(identical): print("Files are identical")
        
