#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_N 100
#define MAX_W (MAX_N * MAX_N * MAX_N)

bool Opt[MAX_N + 1][MAX_W / 2 + 1];

bool can_split_equally(int n, int w[], int total_sum) {
    // Initialize the first row
    for (int j = 1; j <= total_sum / 2; j++) {
        Opt[1][j] = (w[0] == j);
    }

    // Fill the Opt array
    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= total_sum / 2; j++) {
            if (j - w[i-1] >= 1) {
                Opt[i][j] = Opt[i-1][j] || Opt[i-1][j - w[i-1]];
            } else {
                Opt[i][j] = Opt[i-1][j];
            }
        }
    }

    // The final result is in Opt[n][total_sum/2]
    return Opt[n][total_sum / 2];
}

int main() {
    int n = 5;
    int w[] = {3, 2, 4, 1, 5};
    int total_sum = 0;

    for (int i = 0; i < n; i++) {
        total_sum += w[i];
    }

    bool result = can_split_equally(n, w, total_sum);

    printf("Can the companies be split equally? %s\n", result ? "Yes" : "No");

    return 0;
}