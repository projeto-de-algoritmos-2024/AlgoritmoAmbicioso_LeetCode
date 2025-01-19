#include <stdio.h>

int findMinMoves(int* machines, int machinesSize) {
    int total = 0, target, maxMoves = 0, cumulativeBalance = 0;

    for (int i = 0; i < machinesSize; i++) {
        total += machines[i];
    }

    if (total % machinesSize != 0) {
        return -1;
    }

    target = total / machinesSize;

    for (int i = 0; i < machinesSize; i++) {
        int balance = machines[i] - target;
        cumulativeBalance += balance;
        if (maxMoves < abs(cumulativeBalance)) maxMoves = abs(cumulativeBalance);
        if (maxMoves < balance) maxMoves = balance;
    }

    return maxMoves;
}