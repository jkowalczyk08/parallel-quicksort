#!/usr/bin/python3
import random

correctness_input_sizes = [10000, 30000, 120000, 480000, 2000000]
correctness_input_names = ['1c.in', '2c.in', '3c.in', '4c.in', '5c.in']
correctness_output_names = ['1c.out', '2c.out', '3c.out', '4c.out', '5c.out']
time_input_sizes = [10000, 30000, 120000, 480000, 2000000, 8000000, 32000000, 125000000, 500000000]
time_input_names = ['1.in', '2.in', '3.in', '4.in', '5.in', '6.in', '7.in', '8.in', '9.in']
input_file_name ='test.in'
correct_output_file_name = 'test.out'

for (size, name_in, name_out) in zip(correctness_input_sizes, correctness_input_names, correctness_output_names):
    with open(name_in, 'w') as ifile:
        with open(name_out, 'w') as ofile:            
            print(f'Generating input of size {size}')
            # generate input
            input = []
            for i in range(size):
                single_value = random.randint(0, 20000000)
                input.append(single_value)

            # write to input file
            ifile.write(f'{size}\n')
            for i in input:
                ifile.write(f'{i} ')
            ifile.write('\n')

            # write sorted to output file
            input.sort()
            for i in input:
                ofile.write(f'{i} ')
            ofile.write('\n')

for (size, name) in zip(time_input_sizes, time_input_names):
    with open(name, 'w') as ifile:
        print(f'Generating input of size {size}')
        # generate input and write to file
        ifile.write(f'{size}\n')
        for i in range(size):
            single_value = random.randint(0, 20000000)
            ifile.write(f'{single_value} ')
