#include <iostream>
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
void quickSort(int numbers[], int l, int r) {
    if(r - l + 1 < 20) {
        selectionSort(numbers, l, r);
    } else {
        pair<int,int> p = partition(numbers, l, r);
        quickSort(numbers, l, p.first - 1);
        quickSort(numbers, p.second, r);
    }
}

#define MAX_N 2000000

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

int main() {
    int s; cin >> s;
    while(s--) {
        read_input();
        quickSort(numbers,0,n-1);
        print_output();
    }

    return 0;
}