# parallel-quicksort

## Todo:

- [x] Input generator - small, medium, large
- [x] Output verifier
- [x] 3 test files - small, medium, large
- [x] simple solution
- [x] std::thread solution
- [x] openmp solution
- [x] solution speed checker
- [x] pdf with task description
- [x] compilation instruction (makefile/readme with commands)
- [ ] pdf report with results - graphs, descriptions etc


## Usage:

Run `./generate.py` to generate input. Modify config in generate.py file.

Run `./clean.py` to clean generated input and output.

Run `./test_correctness.py` to test if sorting algorithms are correct.

Run `./test_performance.py` to compare the performance of the algorithms.
You can edit the configuration (number of threads and cores) in `test_performance.py` file.

## Compilation and execution:

- g++ -Wall -O3 -o normal.out quicksort.cpp && ./normal.out {0=correctness test, 1=performance test}
- g++ -Wall -pthread -O3 -o std_thread.out std_thread_quicksort.cpp && ./std_thread.out {0=correctness test, 1=performance test} {max_depth}
- g++ -Wall -fopenmp -O3 -o openmp.out openmp_quicksort.cpp && ./openmp.out {0=correctness test, 1=performance test} {number of threads}
