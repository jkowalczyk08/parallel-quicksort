import argparse
import random

def input_in_range(n):
    n = int(n)
    if n < 1 or n > 2000000000:
        raise argparse.ArgumentTypeError(f"{n} is an invalid number of input sets.")
    return n

input_file_names = {
    'small':'small.in',
    'medium':'medium.in',
    'large':'large.in'
}

correct_output_file_names = {
    'small':'correct_small.out',
    'medium':'correct_medium.out',
    'large':'correct_large.out'
}

array_sizes = {
    'small' : [1, 100],
    'medium' : [101, 20000],
    'large' : [20001, 2000000]
}

parser = argparse.ArgumentParser(description='Generates input for sorting')
parser.add_argument('-s', '-sets', type=input_in_range, help='Number (1 - 2 000 000 000) of input sets', required=True)
parser.add_argument('-as', '--arrays-size', choices=['small', 'medium', 'large'], help='Size of generated arrays', required=True)

args = parser.parse_args()
sets = vars(args)['s']
size = vars(args)['arrays_size']

input_file_name = input_file_names[size]
correct_output_file_name = correct_output_file_names[size]
set_inputs = []
set_outputs = []

for i in range(sets):
    array_size = random.randint(array_sizes[size][0], array_sizes[size][1])
    input = []
    for j in range(array_size):
        single_value = random.randint(array_sizes[size][0], array_sizes[size][1])
        input.append(single_value)
    set_inputs.append(input)
    set_outputs.append(sorted(input))

with open(input_file_name, 'w') as file:
    file.write(f"{sets}\n")
    for i in range(sets):
        file.write(f"{len(set_inputs[i])}\n")
        for j in set_inputs[i]:
            file.write(f"{j} ")
        file.write("\n")
        
with open(correct_output_file_name, 'w') as file:
    for i in range(sets):
        for j in set_outputs[i]:
            file.write(f"{j} ")
        file.write("\n")
