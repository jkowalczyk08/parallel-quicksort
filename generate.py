#!/usr/bin/python3
import random
import os.path

output_names = ['1.out', '2.out', '3.out', '4.out', '5.out']
input_sizes = [10000, 40000, 160000, 640000, 2560000, 10240000, 40960000, 163840000]
input_names = ['1.in', '2.in', '3.in', '4.in', '5.in', '6.in', '7.in', '8.in']

subdirectory = 'test_cases'

try:
    os.mkdir(subdirectory)
except Exception:
    pass

for (size, name_in, name_out) in zip(input_sizes[:5], input_names[:5], output_names):
    with open(os.path.join(subdirectory, name_in), 'w') as ifile:
        with open(os.path.join(subdirectory, name_out), 'w') as ofile:            
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

for (size, name) in zip(input_sizes[5:], input_names[5:]):
    with open(os.path.join(subdirectory, name), 'w') as ifile:
        print(f'Generating input of size {size}')
        # generate input and write to file
        ifile.write(f'{size}\n')
        for i in range(size):
            single_value = random.randint(0, 20000000)
            ifile.write(f'{single_value} ')
