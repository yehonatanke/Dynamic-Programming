#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_N 100000

int binary_search(int A[], int low, int high, int key) {
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (A[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return low;
}

int longest_increasing_subsequence(int input[], int n) {
    int A[MAX_N + 2];
    A[0] = INT_MIN;
    for (int i = 1; i <= n + 1; i++)
        A[i] = INT_MAX;

    int lis_length = 0;
    for (int i = 0; i < n; i++) {
        int j = binary_search(A, 0, n + 1, input[i]);
        A[j] = input[i];
        if (j > lis_length)
            lis_length = j;
    }

    return lis_length;
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int input[MAX_N];
    printf("Enter the elements:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &input[i]);

    int result = longest_increasing_subsequence(input, n);
    printf("Length of Longest Increasing Subsequence: %d\n", result);

    return 0;
}