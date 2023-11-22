# parallel-quicksort

## Todo:

- [x] Input generator - small, medium, large
- [x] Output verifier
- [x] 3 test files - small, medium, large
- [x] simple solution
- [ ] std::thread solution
- [ ] openmp solution
- [ ] solution speed checker
- [ ] pdf with task description
- [ ] compilation instruction (makefile/readme with commands)
- [ ] pdf report with results - graphs, descriptions etc


## Usage:

Run `./generate.py` to generate input. Modify config in generate.py file.

Run `./clean.py` to clean generated input and output.

## Compilation and execution:

- g++ -Wall -O3 -o a.out quicksort.cpp && ./a.out {0=correctness test, 1=performance test}
- g++ -Wall -pthread -O3 -o b.out std_thread_quicksort.cpp && ./b.out {0=correctness test, 1=performance test} {max_depth}
- g++ -Wall -fopenmp -O3 -o c.out openmp_quicksort.cpp && ./c.out {0=correctness test, 1=performance test} {number of threads}
