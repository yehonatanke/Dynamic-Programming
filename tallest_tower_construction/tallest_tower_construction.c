#include <stdio.h>
#include <stdlib.h>

#define MAX_N 1000

typedef struct {
    int length;
    int width;
    int height;
} Box;

int compare_boxes(const void* a, const void* b) {
    return ((Box*)b)->length - ((Box*)a)->length;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

int tallest_tower(Box boxes[], int n) {
    int opt[MAX_N];
    int i, j, max_height = 0;

    // Sort boxes by length in descending order
    qsort(boxes, n, sizeof(Box), compare_boxes);

    // Initialize opt array
    for (i = 0; i < n; i++) {
        opt[i] = boxes[i].height;
    }

    // Calculate opt values
    for (i = 1; i < n; i++) {
        for (j = 0; j < i; j++) {
            if (boxes[i].width < boxes[j].width && boxes[i].height < boxes[j].height) {
                opt[i] = max(opt[i], opt[j] + boxes[i].height);
            }
        }
        max_height = max(max_height, opt[i]);
    }

    return max_height;
}

int main() {
    int n, i;
    Box boxes[MAX_N];

    printf("Enter the number of boxes: ");
    scanf("%d", &n);

    printf("Enter length, width, and height for each box:\n");
    for (i = 0; i < n; i++) {
        scanf("%d %d %d", &boxes[i].length, &boxes[i].width, &boxes[i].height);
    }

    int result = tallest_tower(boxes, n);
    printf("The height of the tallest possible tower is: %d\n", result);

    return 0;
}