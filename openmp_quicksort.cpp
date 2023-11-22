#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>
#include <omp.h>
using namespace std;

// sorts numbers from [l;r]
void selectionSort(int numbers[], int l, int r) {
    int i, j, min_idx;

    for (i = l; i < r; i++) {
        min_idx = i;
        for (j = i + 1; j <= r; j++) {
            if (numbers[j] < numbers[min_idx])
                min_idx = j;
        }

        if (min_idx != i)
            swap(numbers[min_idx], numbers[i]);
    }
}

pair<int,int> partition(int numbers[], int l, int r) {
    int pivot = numbers[l + ( rand() % (r-l+1))];
    int i = l;
    int k = l;
    int temp;
    for(int j = l; j <= r; j++) {
        if(numbers[j] == pivot) {
            temp = numbers[k];
            numbers[k] = numbers[j];
            numbers[j] = temp;
            k++;
        }
        else if(numbers[j] < pivot) {
            temp = numbers[j];
            numbers[j] = numbers[k];
            numbers[k] = numbers[i];
            numbers[i] = temp;
            i++; k++;
        }
    }
    pair<int,int> p(i,k);
    return p;
}

// sort numbers from [l;r]
void normal_quicksort(int numbers[], int l, int r) {
    if(r - l + 1 < 20) {
        selectionSort(numbers, l, r);
    } else {
        pair<int,int> p = partition(numbers, l, r);
        normal_quicksort(numbers, l, p.first - 1);
        normal_quicksort(numbers, p.second, r);
    }
}

void omp_quicksort(int numbers[], int l, int r, int min_parallel_size) {
    if(r - l + 1 < 20) {
        selectionSort(numbers, l, r);
    } else {
        pair<int,int> p = partition(numbers, l, r);

        #pragma omp task shared(numbers) if(r - l >  min_parallel_size)
        omp_quicksort(numbers, l, p.first - 1, min_parallel_size);

        #pragma omp task shared(numbers) if(r - l > min_parallel_size)
        omp_quicksort(numbers, p.second, r, min_parallel_size);
    }
}

#define MAX_N 500000000
#define MODE_PRINT_ARRAYS 0
#define MODE_PRINT_TIME 1

int numbers[MAX_N];
int n;

void read_input() {
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
}

void print_output() {
    for(int i = 0; i < n; i++) {cout << numbers[i] << " ";}
    cout << "\n";
}

void print_time(double total_duration) {
    cout << "Total duration is: " << total_duration << "ms\n";
}

int main(int argc, char* argv[]) {
    int mode = atoi(argv[1]);
    int thread_count = atoi(argv[2]);
    omp_set_num_threads(thread_count);
    read_input();

    auto start = std::chrono::steady_clock::now();

    #pragma omp parallel
    {
        #pragma omp single
        omp_quicksort(numbers, 0, n-1, 1000);
    }

    auto end = std::chrono::steady_clock::now();
    double duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    
    if(mode == MODE_PRINT_ARRAYS) {
        print_output();
    }

    if(mode == MODE_PRINT_TIME) {
        print_time(duration);
    }

    return 0;
}