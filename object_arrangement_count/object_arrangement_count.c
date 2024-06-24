#include <stdio.h>
#include <stdlib.h>

#define MAX_N 1000

long long count_arrangements(int n) {
    long long *prev = (long long *)calloc(n + 1, sizeof(long long));
    long long *curr = (long long *)calloc(n + 1, sizeof(long long));
    long long result = 0;

    // Base case
    prev[1] = 1;

    for (int i = 2; i <= n; i++) {
        for (int k = 1; k <= i; k++) {
            curr[k] = k * (prev[k-1] + prev[k]);
        }

        // Swap prev and curr
        long long *temp = prev;
        prev = curr;
        curr = temp;
    }

    // Sum up all arrangements
    for (int k = 1; k <= n; k++) {
        result += prev[k];
    }

    free(prev);
    free(curr);

    return result;
}

int main() {
    int n;
    printf("Enter the number of objects: ");
    scanf("%d", &n);

    long long result = count_arrangements(n);
    printf("Number of possible arrangements for %d objects: %lld\n", n, result);

    return 0;
}